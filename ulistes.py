#!/usr/bin/env python3

import sys
import argparse

from patterns import patterns

def help_header():
    h_gfx = '''
 _.........._     
| |        | | Pentesting username generation tool.
| |        | | -----------------------------------------------
| |    xor | | Takes a given name eg. Bob Smith and outputs
| |________| | a cultivated list of possible usernames for use with brute forcing tools.
|   ______   | 
|  |    | |  | This also comes with a predefined set of patterns to use, however the end user
|__|____|_|__| can add their own or remove existing patterns as they see fit. (See patterns.py)

               usage: ./ulistes.py [OPTINOS] <full name>
               eg: ./ulistes.py Bob Smith

               OPTIONS:
               -o <filename> Writes all results to specified file
               -l Will force name into lowercase. Otherwise case will be preserved
               --append <string> Will append this string to the username
               --prepend <string> Will prepend this string to the username\n'''

    print(h_gfx)

    
def build_names(name):
    username_list = []
    
    # build usernames list based on patterns
    for p in patterns:
        username_list.append(eval(p, {}, {"name": name}))
    
    # if we have appends or prepends
    if args.prepend or args.append:
        for i in range(len(username_list)):
            if args.prepend:
                username_list[i] = args.prepend + username_list[i]

            if args.append:
                username_list[i] = username_list[i] + args.append
    
    return username_list


def main(args):    
    username_list = build_names([x.lower() for x in args.name] if args.lowercase else args.name)
    
    if args.output:
        with open(args.output, 'w') as f:
            for u in username_list:
                f.write(u + '\n')
    else:
        for n in username_list:
            print(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Username generator.")

    parser.add_argument('-o', '--output', type=str, help="Output file.")
    parser.add_argument('-l', '--lowercase', action='store_true', help="Will force name into lowercase. Otherwise case will be preserved")
    parser.add_argument('--append', type=str, help="Optional append to the end of the username.")
    parser.add_argument('--prepend', type=str, help="Optional prepend to the beginning of the username.")
    
    # grab the name
    parser.add_argument('name', nargs='*', help="Full name used to generate a username list.")
    
    # parse the arguments
    args = parser.parse_args()
    
    if not args.name:
        help_header()
        print("[\033[1;31mERROR\033[0;0m] At the very least I need a full name eg: ./ulistes.py Bob Smith\n")
        sys.exit(1)
    
    main(args)