"""@
#Name:pwd
#Description:It displays the present working directory
#parameters:none
"""
import threading
import os
import sys

def pwds():
		print(os.getcwd())
		return