#!/usr/bin/env python
import time
from datetime import datetime
import calendar
import os
import sys
import re

# Argument Parsing for .log path
files = sys.argv[1:]
path = files[0]

print("\nLoading log file from {}".format(path))

# Convert timestamp to UNIX
def getQueryFromTimeStamp(start,end):
    
    StartIdx = calendar.timegm(time.strptime(start,'%Y-%m-%d %H:%M' ))
    StopIdx = calendar.timegm(time.strptime(end,'%Y-%m-%d %H:%M' ))\
    
    return StartIdx,StopIdx

# Load log file
log_data=open(path,'r')
data = {}
for line in log_data:
    columns = line.splitlines() 

    for c in columns:
        ts = (c.split(':')[0])
        tss = datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M')
        ip=c.split(':')[1]
        cpu = c.split(':')[2]
        usage=(c.split(':')[3])

        if ip not in data:
            data[ip]={}
        if cpu not in data[ip]:
            data[ip][cpu]={}
                
        data[ip][cpu][int(ts)]=(tss+", "+str(usage)+"%")
# Display
print('**********************************************************************************\n\n                           This is a Query Engine.\n\nCommands for Query:\n1)QUERY <serverIP> <cpuID> <time-start> <time-end>\n2)EXIT\n\n**********************************************************************************')

# Engine
isOn = True

# Regex for Valid TimeStamp
r = re.compile(r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[01]) (2[0-3]|[01][0-9]):[0-5][0-9]')

while isOn:

	s = input(">")
	S = s.split(" ")
	isValid = False
	isValidTimeStamp = False

	# feature for exit
	if S[0]=="EXIT":
		break
	elif not isValid and len(S)==7:
		ip = S[1]
		cpu = S[2]
		start_time = S[3]+" "+S[4]
		end_time = S[5] + " " + S[6]

		# check for valid TimeStamp
		if r.match(start_time) is None:
			print ('Error: Invalid Start Time\nTime Format must be YYYY-MM-DD HH:MM\n')
		elif r.match(end_time) is None:
			print ('Error: Invalid End Time\nTime Format must be YYYY-MM-DD HH:MM\n')
		else:
			isValidTimeStamp=True


		# if isValidTimeStamp:
		if isValidTimeStamp:
			UnixStart , UnixStop = getQueryFromTimeStamp(start_time,end_time)
		# check for Valid IP CPU UNIX start stop
			if ip not in data:
				print("Error: Invalid IP\n")
			
			elif cpu not in data[ip]:
				print("Error: Invalid CPU ID\n")

			elif int(UnixStart) not in data[ip][cpu]:
				print("Error: Invalid Start Time\n")
			# 	
			elif int(UnixStop) not in data[ip][cpu]:
				print("Error: Invalid Stop Time\n")

			elif int(UnixStop) < int(UnixStart):
				print("Error: Stop Time must be greater than Start Time\n")

			# You are here if all valid entries
			else:
				isValid=True
		
	# Error 
	elif s:
		print("Error: Invalid Query:\nQuery should be in format \n>QUERY <serverIP> <cpuID> <time-start> <time-end>")
	

	# feature for query
	if S[0]=="QUERY" and len(S)==7 and isValid:

		res = []
		x = data[ip][cpu]

		for i in range(UnixStart,UnixStop+60,60):
			res.append(str(x[i]))
		print("CPU{} usage on {}:\n(".format(cpu,ip)+"),(".join(res)+")")
		res=[]