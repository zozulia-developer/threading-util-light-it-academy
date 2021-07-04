""" Util for copy or move files with threads """
import os
import shutil
import argparse
import logging
from threading import Thread, Semaphore

logging.basicConfig(filename='logs.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


def _deep_copy(src: str, to: str, s: Semaphore) -> None:
    """ Copy files with directories """
    extension = _check_pattern(src)
    src_path = src.split('*')[0]
    files = os.listdir(src_path)
    for file in files:
        if extension and file.endswith(extension):
            t = Thread(target=_copy(src_path + file, to + file), args=(s,))
            t.start()
        if not extension and os.path.isfile(src_path+file):
            t = Thread(target=_copy(src_path+file, to+file), args=(s,))
            t.start()
        if os.path.isdir(src_path+file):
            try:
                shutil.copytree(src_path+file, to+file)
                logging.info('Directory %s deep copied to %s successfully!', file, to+file)
            except FileExistsError:
                logging.warning('Directory %s already exists!', to+file)


def _copy(src: str, to: str) -> None:
    """ Copy file with logging """
    if os.path.isfile(src):
        shutil.copy2(src, to)
        logging.info('File copied from %s to %s successfully!', src, to)


def _check_pattern(path: str) -> str:
    """ Check if path contains symbol '*' """
    return path.split('*')[1] if '*' in path else None


def copy_files(from_path: str, to_path: str, s: Semaphore) -> None:
    """ Copy files from source path to destination path """
    try:
        _deep_copy(from_path, to_path, s)
    except FileNotFoundError as e:
        print(e)


def move_files(from_path: str, to_path: str, s: Semaphore) -> None:
    """ Move files from source path to destination path """
    extension = _check_pattern(from_path)
    src_path = from_path.split('*')[0]
    files = os.listdir(src_path)
    try:
        for file in files:
            if extension and file.endswith(extension):
                t = Thread(target=shutil.move(from_path + file, to_path), args=(s,))
                t.start()
                logging.info('File %s moved from %s to %s successfully!', file, from_path, to_path)
            else:
                t = Thread(target=shutil.move(from_path + file, to_path), args=(s,))
                t.start()
                logging.info('File %s moved from %s to %s successfully!', file, from_path, to_path)
    except FileNotFoundError as e:
        print(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--operation', help='select operation, move or copy')
    parser.add_argument('-f', '--FROM', help='select path where from to do operation')
    parser.add_argument('-t', '--TO', help='select path where to do operation')
    parser.add_argument('-thr', '--threads', type=int, default=1, help='select number of threads')
    args = parser.parse_args()
    s = Semaphore(args.threads)
    logging.info('Amount of Semaphores - %s', args.threads)

    if args.operation == 'copy':
        copy_files(args.FROM, args.TO, s=s)
    elif args.operation == 'move':
        move_files(args.FROM, args.TO, s=s)
    else:
        logging.error("'%s' is Incorrect operation!", args.operation)


if __name__ == '__main__':
    main()
