""" @
Name:Who
#Description:It displays the present user who is working on it
#parameters:none
"""
import threading
import os
import sys


def who():
	print(os.popen('who').read())