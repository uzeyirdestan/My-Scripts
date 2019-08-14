#!/usr/bin/python
from threading import Thread
from Queue import Queue
import os
import re
import sys
queue = Queue()
def scan(que):
	while True:
		domain=que.get()
		command = "whois %s | grep -iE '%s'"%(domain,sys.argv[2])
		output=os.popen(command).read()
		if len(output) > 0:
			print domain
		que.task_done()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "[+] Usage is %s <domainlist> <keyword> " % sys.argv[0]
		print "example : %s googlesublist google"
	with open(sys.argv[1]) as f:
		for line in f:
			queue.put(line.rstrip('\n'))
	for i in range(10):
		t = Thread(target=scan, args=(queue,))
		t.daemon = True
		t.start()
	queue.join()
