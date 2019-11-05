#!/usr/bin/python3

import sys
import random
import argparse

COMMON_BG = "авгеиКкмМнопрсТтух"
COMMON_EN = "aBreuKkMMHonpcTTyx"

def voidscate(text, rev=False):
    temp = ""
    if rev:
        this, that = COMMON_BG, COMMON_EN
    else:
        this, that = COMMON_EN, COMMON_BG

    for letter in text:
        if letter in list(this):
            for i,j in enumerate(list(this)):
                if j == letter:
                    letter = that[i]
        temp += letter
    
    return temp

def get_args(args):
    '''
    Helper function for parsing arguments
    
    Usage:
        args = get_args(sys.argv)
    '''
    old_argv = sys.argv
    sys.argv = args

    parser = argparse.ArgumentParser(
                description = 'Welcome to translateVoid.py')

    parser.add_argument('-s', '--string', dest = 'sentence',
                        help = 'Passing an escaped strings')

    parser.add_argument('-c', '--clipboard', dest = 'clipboard', action='store_true',
                        help = 'Grab a string from the clipboard')
    
    parser.add_argument('-r', '--reverse', dest = 'reversed', action='store_true',
                        help = 'Substitute characters from string based on cyrilic characters')

    args = parser.parse_args()

    sys.argv = old_argv
    globals().update(vars(args))
    return args

if __name__ == "__main__":
    args = get_args(sys.argv)
    if args.clipboard:
        # Grab from clipbard
        print('Clipboard plugin is not available right now')
        sys.exit(1)

    if args.sentence:
        # Parse the string
        result = voidscate(args.sentence, rev=args.reversed)
        print(result)

    pass