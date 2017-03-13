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
				
				lines=lines+1
				print line.strip()
	else:
		print("file doesnt exists")
