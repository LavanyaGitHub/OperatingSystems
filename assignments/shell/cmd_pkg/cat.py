"""@
Name:cat
#Description:It displays the content of given file
#parameters:filename
"""
#!/usr/bin/env python
import os
import sys
import threading

def cat(filename):
	if os.path.exists(filename):
		f = open(filename, "r")
		text = f.read()
		print text
		f.close()
	else:
		print("File doesn't exist")