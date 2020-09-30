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
            # print(commands[counter])
            instructions.append(f'{item} {command}')
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
            # print(commands[counter])
            instructions.append(f"{item} {command}")
    directions = ('\n'.join(instructions))
    dothis = "echo " + "'" + directions + "'" + " >> ./server/instructions.txt"
    # return(dothis)
    os.system(dothis)
    
    # return(directions)

    # return('\n'.join(instructions))



if __name__ == '__main__':
    do_what = sys.argv[1]
    # print(do_what)
    bots = sys.argv[2]
    # print(bots)
    commands = sys.argv[3]
    # print(commands)

    if do_what == 'replace':
        bots = sys.argv[2]
        commands = sys.argv[3]
        replace_commands(bots, commands)
    elif do_what == 'append':
        bots = sys.argv[2]
        commands = sys.argv[3]
        append_commands(bots,commands)
    elif do_what == 'clear':
        clear()
    elif do_what == '-h' or '--help':
        help_me()
