"""@
#Name:rm
#description:deletes the file 
parameters:file to be removed
"""
import threading
import os
import sys

def rm(file):
        if(os.path.isfile(file)):
            os.remove(file)
            print("file removed succesfully")
        else:
            print("file does not exist")