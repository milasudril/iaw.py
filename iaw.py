#!/usr/bin/python3

import inotify.adapters
import sys
import time
import subprocess

def listen_on_dev_input(timeout, command):
	i = inotify.adapters.Inotify(block_duration_s = timeout)
	i.add_watch('/dev/input')
	start = time.monotonic_ns()
	proc = None
	for event in i.event_gen():
		now = time.monotonic_ns()
		if event == None:
			if now - start >= timeout*1e9:
				if proc == None:
					proc = subprocess.Popen(command)
		else:
			(_, type_names, path, filename) = event
			if filename != '':
				if proc != None
					proc.terminate()
					proc = None
				start = now

def main(argv):
	listen_on_dev_input(timeout = float(argv[1]), command = argv[2:])

if __name__ == '__main__':
	main(sys.argv)
