""" Util for copy or move files with threads """
import os
import shutil
import argparse
from threading import Thread, active_count


def copy_files(from_path: str, to_path: str, threads_number=1) -> None:
    files = os.listdir(from_path)
    try:
        for f in files:
            shutil.copy2(from_path + f, to_path)
            print(f"File {f} copied from {from_path} to {to_path} successfully!")
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
