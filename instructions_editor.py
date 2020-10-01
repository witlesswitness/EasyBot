#!/usr/bin/env python3
import sys
import os

def help_me():
    dothis = "echo 'Use Direditor as such: first argument is the command to execute: clear, append, or replace. Append and replace must have two additional arguments: bots to instruct, followed by commands to execute'"
    # return(dothis)
    os.system(dothis)

def clear():
    dothis = "echo -n '' > ./server/instructions.txt"
    # return(dothis)
    os.system(dothis)
    
    

def replace_commands(s1,s2):
    bots = s1.strip().split(',')
    commands = s2.strip().split(',')
    # print(commands)
    instructions = []
    for item in bots:
        # print(item)
        for command in commands:
            addon = ">> sendthis.txt"
            # print(commands[counter])
            instructions.append(f'{item} {command} {addon}')
    directions = ('\n'.join(instructions))
    dothis = "echo " + "'" + directions + "'" + " > ./server/instructions.txt"
    # return(dothis)
    os.system(dothis)
    # return(directions)
    # return('\n'.join(instructions))
    
def append_commands(s1,s2):
    bots = s1.strip().split(',')
    commands = s2.strip().split(',')
    # print(commands)
    instructions = []
    for item in bots:
        # print(item)
        for command in commands:
            addon = ">> sendthis.txt"
            # print(commands[counter])
            instructions.append(f"{item} {command} {addon}")
    directions = ('\n'.join(instructions))
    dothis = "echo " + "'" + directions + "'" + " >> ./server/instructions.txt"
    # return(dothis)
    os.system(dothis)
    
    # return(directions)

    # return('\n'.join(instructions))

def main(s1,s2,s3):
    do_what = s1
    bots = s2
    commands = s3
    if do_what == 'replace':
        replace_commands(bots, commands)
    elif do_what == 'append':
        append_commands(bots,commands)
    elif do_what == 'clear':
        clear()
    elif do_what == '-h' or '--help':
        help_me()

if __name__ == '__main__':
    
    do_what = sys.argv[1]
    if do_what == 'clear':
        bots = 0
        commands = 0
    if do_what != 'clear':
        bots = sys.argv[2]
        commands = sys.argv[3]

    main(do_what, bots, commands)
