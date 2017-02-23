"""@#Name:less
#Description:displays a file in a page at a time
#parameters:filename
"""

import threading
import os
import sys

def less(filename):
	if os.path.exists(filename):                                           
		f = open(filename, "r")
		text = f.readline()
		lines=0
		for line in f:
			if lines==5:	
				user = raw_input("press enter to continue..")
				if user == "":
					lines = 0
					continue
				else:	
					break
			else :
				print line
				lines=lines+1
	else:
		print("file doesnt exists")