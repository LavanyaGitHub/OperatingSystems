"""@
Name: ls
#Description:It displays the existing files and directories
#parameters:none 
"""
import threading
import os
import sys
from subprocess import check_output


def ls():
                

			list=os.listdir(os.getcwd())
			list.sort()
			for i in list:
				if i.startswith('.'):
					list.remove(i)
			for i in list:
				print(i)
                       