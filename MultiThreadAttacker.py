#!/usr/bin/python

import socket;
import threading;

class AttrackerThread(threading.Thread):
	
	#Initiate the thread.
	def __init__(self,threadID, passwrds, servaddr,servport):
		threading.Thread.__init__(self);
		self.threadID = threadID;
		self.password = passwrds;
		self.servAddr = servaddr;
		self.servPort = servport;

#	#Fetch the its own part passwords from the the 'passwords' string list Given by Caller.
#	def fetchPasswords(passs):
#		passwords = passwrds;
#		print 'Fetch' + len(passwords) + 'password record successfully';
#		return;

	#Start to try every password in the 'passwords'.
	def startAttack():
		for index in range(len(passwords)):
			print self.threadID + ':' + index +'th password.';
			clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
			clientSocket.connect((serveripaddr, serverpors));
			clientSocket.send('Samuel '+passwords[index]);
			authInfo = clientSocket.recv(100);
			if authInfo =='OK':
				print 'Find Successful:' + passwords[index];
				break;
		print 'Finish but no Answer';
		return;

	#Overrided run function
	def run(self):
		print 'Starting:' + self.threadID;
#		fetchPassword();
		startAttack();
		print 'Stop:' + self.threadID;

# fetch the file<./self.threadID.txt> and parse it into N string lists.
def 
