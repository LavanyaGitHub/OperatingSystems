"""@
#Name:sort
#Description:sorts the contents of a text file, line by line
#parameters:file
"""
import threading
import os
import sys

def sort(file):
	 if os.path.exists(file):
		with open(file) as f:
			for line in sorted(f):
        			print (line)
	 else:
		print("file doesnt exist")