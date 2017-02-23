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
			dir_contents = check_output(['ls'])
			print dir_contents