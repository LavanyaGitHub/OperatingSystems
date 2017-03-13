"""@
#Name:rmdir
#Description:deletes the directory
#parameters:directory to be removed
"""
import threading
import os
import sys
import shutil

def rmdir(directory):
	if not os.path.exists(directory):
		print("directory is not present")
	else:
		shutil.rmtree(directory)
		print(" directory has been removed")