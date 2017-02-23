"""@
#Name:cp
#Description:copies the contents of one file to other
#parameters:filename1,filename2
"""

import threading
import os
import sys

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