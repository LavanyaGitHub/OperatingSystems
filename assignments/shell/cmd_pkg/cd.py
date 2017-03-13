"""@
#Name:cd
#Description:cd- directory:changes to specified-directory,
#cd..-change to parent directory,c
#d~-change to home-directory
@parameters: directory
"""
import threading
import os
import sys

def cd(directory):
        if directory=='..':
            os.chdir('..')
            new=os.getcwd()
            print(new)
        elif directory=='~':
            home=os.path.expanduser('~')
            os.chdir(home)
            new=os.getcwd()
            print(new)
        else:
            if os.path.isdir(directory):
                os.chdir(directory)
                new=os.getcwd()
                print(new)
            else:
                print("directory  does not exist")