""" Util for copy or move files with threads """
import os
import shutil
import argparse
import threading


def copy_files(from_path, to_path):
    try:
        shutil.copy2(from_path, to_path)
    except FileNotFoundError:
        pass


def move_files(from_path, to_path):
    try:
        shutil.move(from_path, to_path)
    except FileNotFoundError:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--operation', help='select operation, move or copy')
    parser.add_argument('-f', '--from', help='select path where from to do operation')
    parser.add_argument('-t', '--to', help='select path where to do operation')
    parser.add_argument('-thr', '--threads', type=int, help='select number of threads')
    args = parser.parse_args()
    print(args)

    if args.operation == 'copy':
        copy_files(args.FROM, args.TO)
    elif args.operation == 'move':
        move_files(args.FROM, args.TO)


if __name__ == '__main__':
    main()
