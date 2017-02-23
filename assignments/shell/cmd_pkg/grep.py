
"""@
Name :grep
#Description:It searches for the keywords in the given file
#parameters:filename and keyword to search
"""
import threading
import os
import sys


def grep(filename,searchphrase):
	 if os.path.exists(filename):
	 	searchfile = open(filename)
		for line in searchfile:
   		 if searchphrase in line: 
			print line
		searchfile.close()
	 else:
		print("file doesnot exist")