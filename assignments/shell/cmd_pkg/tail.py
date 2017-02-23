
""" @
Name:tail
#Description:It displays the last n number of lines in the given file
#parameters:filename
"""
import threading
import os
import sys

def tail(filename):
	 if os.path.exists(filename):
		nlines=-10
		lines=open(filename,'r').readlines()
		tot_lines = len(lines)
      		for i in range(nlines,0):
        		print lines[i]
	 else:
		print("file doesnt exists")