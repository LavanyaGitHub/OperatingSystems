"""@
#Name:mv
#Description:moves the contents of one file to other and deletes the original file
#defined: copy and remove
#parameters:filename1,filename2
"""
import threading
import os
import sys
import subprocess
from cmd_pkg import cp
from cmd_pkg import rm

def cp(filename1,filename2):
        path=os.getcwd()
        conc=path+'\%s'%filename1
        if os.path.exists(filename1):
        	fread=open(filename1,'r')
                content=fread.read()
                fread1=open(filename2,'w')
                fread1.write(content)
		print("succesfully made a copy of the file")
                fread.close()
                fread1.close() 
	else:
		print("file doesnt exist") 
def rm(file):
        if(os.path.isfile(file)):
            os.remove(file)
            print("file removed succesfully")
        else:
            print("file does not exist")
def mv(filename1,filename2):
	 if(os.path.isfile(filename1)):
		cp(filename1,filename2)
		rm(filename1)
		print "Moved the file"
	 else:
		print("files doesnt exist")
		