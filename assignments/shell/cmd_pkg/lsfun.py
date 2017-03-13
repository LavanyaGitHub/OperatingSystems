
"""@
#Name:ls-a,ls-l
#Description:ls-a: displays all hidden files
#ls-l: long listing
#parameters:flag (The command to be executed in within ls)
"""
import os
import sys
import shutil
import math
import time
import threading
import stat
import shlex
#import pwd
from stat import *
#from pwd import getpwuid
#from pwd import getpwuid
from os import stat
def binary(p):
		if p==777:
			return "rwxrwxrwx"
		if p==444:
			return "rrrrrrrrr"
		if p==555:
			return "r-xr-xr-x"
		if p==666:
			return "rw-rw-rw-"
		if p==765:
			return "rwxrw-r-x"
		if p==755:
			return "rwxr-xr-x"
		if p==756:
			return "rwxr-xrw-"
		if p==644:
			return "rw-r--r--"

def lsfun(flag):
	op=open("op.txt",'w')
	if flag==0:
		list=os.listdir(os.getcwd())
		list.sort()
		for i in list:
			if i.startswith('.'):
				list.remove(i)
		for i in list:
			print(i) 
	elif flag=='-a':
			list=os.listdir(os.getcwd())
			list.sort()
			for i in list:
				print(i) 
	elif flag=='-lah':
	    a=['File Name','Size','Permissions','Accessed','Modified','Changed']
	    list1=[]
            list2=[]
            list=os.listdir(os.getcwd())
            print('  {0:16s}   {1:9s}   {2:12s}   {3:24s}   {4:24s}   {5:24s} '.format(a[0],a[1],a[2],a[3],a[4],a[5]))
            print('{0:16s}   {1:9s}   {2:12s}   {3:24s}   {4:24s}   {5:24s}'.format("-----------","---------","-------------","----------------","-------------------","-------------------","-------------------"))
			#for i in list:
			#	f=os.stat(os.getcwd()+"/%s"%i)
			#	for i in range(0,len(list1)):
            for k in list:
                          		f=os.stat(os.getcwd()+"/%s"%k)
                          		st1=os.stat(k)
				#if flag=='-l':
                                 #       temp1=list2[0]
                                #if list1[i]==temp1:
                                        Size=size_convert(f.st_size)
                                        Perm=int(oct(os.stat(k)[ST_MODE])[-3:])
                                        Atime=time.asctime(time.localtime(st1[ST_ATIME]))
                                        Mtime=time.asctime(time.localtime(st1[ST_MTIME]))
                                        Ctime=time.asctime(time.localtime(st1[ST_CTIME]))
                                        print('  {0:16s}   {1:8s}   {2:12d}   {3:24s}   {4:24s}   {5:24s} '.format(k,Size,Perm,Atime,Mtime,Ctime))
"""
@Name: size_convert
        @Description:
                converts the size of the files
        @Params:
                size (string) - size of the file
        @Returns:
                returns size of the file
        """        
def size_convert(size):
                suffixes=['B','KB','MB','GB','TB']
                precision=3
                suffixIndex = 0
                while size > 1024 and suffixIndex < 4:
                        suffixIndex += 1 #increment the index of the suffix
                        size = size/1024.0 #apply the division
                return "%.*f%s"%(precision,size,suffixes[suffixIndex])
