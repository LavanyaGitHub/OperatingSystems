"""@
#Name:pwd
#Description:It displays the present working directory
#parameters:none
"""
import threading
import os
import sys

def pwd():
		print(os.getcwd())
		return