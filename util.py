""" Util for copy or move files with threads """
import os
import shutil
import argparse
from threading import Thread, active_count


def _is_dir(files: list, src: str, to: str) -> None:
    for f in files:
        print(os.path.isdir(src+f))
        if os.path.isdir(src+f):
            if not os.path.exists(to+f):
                os.mkdir(to+f)
                print(f'Make new directory in {to} successful!')
            files_in_dir = os.listdir(src+f)
            return _is_dir(files_in_dir, src + f + '/', to + f + '/')
        _copy(src+f, to+f)


def _copy(src: str, to: str) -> None:
    if os.path.isfile(src):
        shutil.copy2(src, to)
        print(f'File copied from {src} to {to} successfully!')


def copy_files(from_path: str, to_path: str, threads_number=1) -> None:
    files = os.listdir(from_path)
    print(files)
    try:
        for f in files:
            _is_dir(files, from_path, to_path)
            _copy(from_path+f, to_path+f)
    except FileNotFoundError:
        pass


def move_files(from_path: str, to_path: str, threads_number=1) -> None:
    files = os.listdir(from_path)
    try:
        for f in files:
            shutil.move(from_path + f, to_path)
            print(f"File {f} moved from {from_path} to {to_path} successfully!")
    except FileNotFoundError:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--operation', help='select operation, move or copy')
    parser.add_argument('-f', '--FROM', help='select path where from to do operation')
    parser.add_argument('-t', '--TO', help='select path where to do operation')
    parser.add_argument('-thr', '--threads', type=int, help='select number of threads')
    args = parser.parse_args()
    print(args)

    if args.operation == 'copy':
        copy_files(args.FROM, args.TO)
    elif args.operation == 'move':
        move_files(args.FROM, args.TO)


if __name__ == '__main__':
    main()
