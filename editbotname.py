#!/usr/bin/env python3
import sys
import os


def pull_botnames_inlogs():
    
    with open('/home/kali/project/webserver/directory/logs.txt') as input_file:
        bots = []
        for line in input_file:
            # print(line)
            # print(bots)
            section=line.strip().split()
            if len(section) >= 3:
                if section[1] == '/botnames.txt':
                    bots.append(section[2].strip().split(':')[1])
        checkname(bots)


def checkname(l1):
    for item in l1:
        # print(item)
        counter = 0
        command = ''
        with open('/home/kali/project/webserver/directory/botnames.txt') as input_file:
            
            for line in input_file:
                if line.strip() == item.strip():
                    counter +=1
                else:
                    counter +=0
            if counter == 0:
                command = 'echo ' + item + ' >> /home/kali/project/webserver/directory/botnames.txt'
                os.system(command)

def main():
    pull_botnames_inlogs()

if __name__ == '__main__':    
    main()
