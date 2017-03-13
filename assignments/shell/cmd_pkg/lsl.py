import threading
import os
import sys
import stat
import time
import shutil
import subprocess
import shlex



def lsl(flag):
        files_list=[]
        for filename in os.listdir('.'):
            file_stats=os.stat(filename)
            file_list = [
            filename,
            file_stats [stat.ST_SIZE],
            oct(stat.S_IMODE(file_stats.st_mode)),
            time.strftime("%b:%d:%Y %H:%M:%S", time.gmtime(os.path.getmtime(filename))),
            time.strftime("%b:%d:%Y %H:%M:%S", time.gmtime(os.path.getatime(filename))),
            time.strftime("%b:%d:%Y %H:%M:%S", time.gmtime(os.path.getctime(filename)))
            ]
            files_list.append(file_list)
	if(flag=='-l'):
          print '{0:20} {1:8} {2:10} {3:35} {4:10} {5:25}'.format("FileName","Size","Permission","ModifyTime","AccessTime","CreationTime")
          print '{0:20} {1:8} {2:10} {3:35} {4:10} {5:25}'.format("---------","---------","--------","--------","--------","--------")
          for file in files_list:
              print '{0:20} {1:5} {2:10} {3:15} {4:5} {5:25}'.format(file[0],file[1],file[2],file[3],file[4],file[5])

	else:
            print("flag is not recognised")
