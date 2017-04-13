"""
Report: 
Project Title: Shell Implementation
Date : 02/ 23/ 2017
Group :	        1.Lavanya Mengaraboina
		2.Shaila Mogalapu
		3.Keerthi Reddy Gangidi
Commands Implemented: 
1. ls                           8.  rm                     15. wc                               22.!x
2. ls -l                        9.  rmdir                  16. command1 | command2              23.cmnd > file
3. mkdir                        10. cat                    17. cat file1 file2 > file0		24.cmnd < file
4. cd (directory, ~, ..)        11. less                   18. sort				25.cmnd >> file
5. pwd                          12. head                   19. who				26.cmd1 | cmd2
6. cp                           13. tail                   20. history				27.ls -lah
7. mv                           14. grep                   21. chmod				28.ls -a

Instructions to run the shell:
To run driver.py :  python driver.py
After % symbol is displayed, enter the command to be executed (from commands implemented)
If you want to continue enter the next command, else type exit() to exit shell.


#Description: Main function through which all the commands are invoked
"""
#!/usr/bin/env python
import threading
import os
import sys
import stat
import time
import shutil
import subprocess
from cmd_pkg import commands

command_history = []
command_new=[]
number_command = []
new=[]
c = []
"""
#Description: Redirect input from a file
"""
def inputredirect(cmd,file):
        new_c=cmd+" "+file

        runshell(new_c)
"""
#Description: Append 
"""
def appendd(cmd,filedest):
	
		save = sys.stdout
                f = open('output.log', 'w')
                sys.stdout = f
                runshell(cmd)
                sys.stdout = save
                f=open('output.log','r')
                content=f.read()
                fread1=open('copy','w')
		f1=open('output.log','r')
                fread1.write(content)
		content1=f1.read()
                fread2=open(filedest,'a')
                fread2.write(content)
                f.close()
                fread1.close()

"""
#description: displays all the commands that were executed
"""
def history():
		new=list(enumerate(command_history))
		for i,v in enumerate(command_history,start=0):
			print i,v
	
"""
#description: output of one command as the input of other command
#parameters: two commands 
"""
def piping(cmd,cmd1):
	        save = sys.stdout
                f = open('output.log', 'w')
                sys.stdout = f
                runshell(cmd)
                sys.stdout = save
                f=open('output.log','r')
                content=f.read()
                fwrite=open('file.txt','w')
                fwrite.write(content)
                f.close()
                fwrite.close()
		new=cmd1 +" "+ "file.txt"
		print new
		runshell(new)
		#print "back"
		
"""
#description: redirects the output of the command to a  file
#parameters: command ,>, file name
"""
def redirect(cmd1,file):
		save = sys.stdout
                f = open('output.log', 'w')
                sys.stdout = f
                runshell(cmd1)
                sys.stdout = save
                f=open('output.log','r')		
                content=f.read()
                fwrite=open(file,'w')
                fwrite.write(content)
		f.close()
                fwrite.close()
"""
#Description: !x
"""

def previoushistory(cmd):
	x1=[]
	y=[]
	x1=list(cmd)
	del x1[0]
	files=''.join(x1)
	files=eval(files)
	new=list(enumerate(command_history))
	y=new[files]
	newcmd= y[1].strip(" ")
	print newcmd
	runshell(newcmd)
"""
#Description: specifies redirect and the pipe commands their functionality according to the given input
"""
def input():
	 cmd = raw_input("%" )
	 runshell(cmd)
	 
"""
#Description: Invoking all the defined commands using threading
"""
def runshell(cmd):
	  parts = []
	  parts1=[]
	  x=[]
	  parts=cmd.split(" ")
	  parts1=parts
	  command_history.append(cmd)
	  command_new.append(parts[0])
	  x=list(parts[0])
	  if '>>' in cmd and len(parts)!=5:
		 c=cmd.split(">")
		 c[0]=c[0].strip(" ")
		 c[2]=c[2].strip(" ")
		 t=threading.Thread(target=appendd,args=(c[0],c[2],))
		 t.start()
		 t.join()
	  elif '>' in cmd and parts[0]!='grep':
            c=cmd.split(">")
            if len(parts)!=5 and len(parts)!=7 and len(parts)!=2:
                 c[0]=c[0].strip(" ")
                 c[1]=c[1].strip(" ")
                 t=threading.Thread(target=redirect,args=(c[0],c[1],))
                 t.start()
                 t.join()
            elif len(parts)==7:
                 c1=cmd.split(">")
                 new_cmd=[]
                 c1[0]=c1[0].strip(" ")
                 c1[1]=c1[1].strip(" ")
                 new_cmd=c1[0].split(" ")
                 c1[2]=c1[2].strip(" ")
                 t=threading.Thread(target=commands.cat1.cat1,args=(new_cmd[1],new_cmd[2],c1[2],))
                 t.start()
                 t.join()
	    elif (len(parts)==5):
                 file1=parts[1]
                 file2=parts[2]
                 file3=parts[4]
                 c=threading.Thread(target=commands.cat1.cat1,args=(file1,file2,file3,))
                 c.start()
		 c.join()
#	    else:
#		print "out of range"
	  elif '|' in cmd:
		 c=cmd.split("|")
		 c[0]=c[0].strip(" ")
		 c[1]=c[1].strip(" ")
		 file1=str(c[0])
		 file2=str(c[1])
		 t=threading.Thread(target=piping,args=(file1,file2,))
		 t.start()
		 t.join()
	  elif '<' in cmd:
                p=cmd.split("<")
                p[0]=p[0].strip(" ")
                p[1]=p[1].strip(" ")
                c=threading.Thread(target=inputredirect,args=(p[0],p[1],))
                c.start()
                c.join()
	  elif parts[0]=='rm':
                if(len(parts)==1) | (len(parts)>2):
                  print("invalid rm command")
                elif(len(parts)==2):
                   files=parts[1]
		   c=threading.Thread(target=commands.rm.rm,args=(files,))
		   c.start()
		   c.join()
	  elif parts[0] == 'pwd':
			c = threading.Thread(target=commands.pwds.pwds)
			c.start()
			c.join()
	  elif parts[0] == 'mv':
			file1 = parts[1]
			file2 = parts[2]
			c = threading.Thread(target=commands.mv.mv, args=(file1, file2,))
			c.start()
			c.join()
	  elif parts[0]=='tail':
		     c=threading.Thread(target=commands.tail.tail,args=(parts[1],))
		     c.start()
		     c.join()
	  elif parts[0]=='grep':
                if len(parts)==3:
                     c=threading.Thread(target=commands.grep.grep,args=(parts[2],parts[1],))
                     c.start()
                     c.join()
                elif len(parts)==5:
                        c=cmd.split(">")
                        c[0]=c[0].strip(" ")
                        c[1]=c[1].strip(" ")
                        c=threading.Thread(target=redirect,args=(c[0],c[1],))
                        c.start()
                        c.join()
	  elif '!' in cmd:
		     c=threading.Thread(target=previoushistory,args=(parts[0],))
		     c.start()
		     c.join()
	  elif parts[0]=='ls':
	#	print "in lsfun"
                if(len(parts)==1):
                    c=threading.Thread(target=commands.ls.ls)
		    c.start()
		    c.join()
                elif (len(parts)==2) and parts[1]!='-l':
		    files=parts[1]
                    c=threading.Thread(target=commands.lsfun.lsfun,args=(files,))
		    c.start()
		    c.join()
		elif parts[1]=='-l':
         #           print "in ls"
                    files=parts[1]
                    c=threading.Thread(target=commands.lsl.lsl,args=(files,))
                    c.start()
                    c.join()

	  elif parts[0]=='history':
           if len(parts)==1:
              c=threading.Thread(target=history)
	      c.start()
	      c.join()
           else:
	      print("Needs only 1 arguments")
	  elif parts[0] == 'who':
		c = threading.Thread(target=commands.who.who)
		c.start()
		c.join()
	  elif parts[0]=='cd':
                if (len(parts)==1) | (len(parts)>2):
                   print("invalid command")
                elif(len(parts)==2):
                    files=parts[1]
		    c=threading.Thread(target=commands.cd.cd,args=(files,))
		    c.start()
		    c.join()
	  elif parts[0] == 'cat':
		if (len(parts)==1) | (len(parts)>2):
                   print("invalid command")
		elif (len(parts)==2):
			file = parts[1]
			c = threading.Thread(target=commands.cat.cat, args=(file,))
			c.start()
			c.join()
	  
          elif parts[0] == 'chmod':
		 if (len(parts)==1) | (len(parts)>3):
                   print("invalid command")
		 elif len(parts)==3:
			flag1 = parts[1]
			flag2 = parts[2]
			c = threading.Thread(target=commands.chmod.chmod, args=(flag1, flag2,))
			c.start()
			c.join()			
	  elif parts[0] == 'cp':
		if (len(parts)==1) | (len(parts)>3):
                   print("invalid command")
		else:
			file1 =parts[1]
			file2 = parts[2]
			c = threading.Thread(target=commands.cp.cp, args=(file1,file2,))
			c.start()
			c.join()
	  elif parts[0]=='wc':
                if(len(parts)==1) | (len(parts)>2):
                  print("invalid command")
                elif(len(parts)==2):
		    files=parts[1]
		    c=threading.Thread(target=commands.wc.wc,args=(files,))
                    c.start()
		    c.join()
	  elif parts[0]=='sort':
		if (len(parts)==1) | (len(parts)>2):
                   print("invalid command")
		else:
			files=parts[1]
			c=threading.Thread(target=commands.sort.sort,args=(files,))
			c.start()
			c.join()
	  elif parts[0]=='head':
		if (len(parts)==1) | (len(parts)>2):
                   print("invalid command")
		else:
			files=parts[1]
			c=threading.Thread(target=commands.head.head,args=(files,))
			c.start()
			c.join()
	  elif parts[0] == 'mkdir':
		if (len(parts)==1) | (len(parts)>2):
                   print("invalid mkdir command")
		else:
			files = parts[1]
			c = threading.Thread(target=commands.mkdir.mkdir,args=(files,))
			c.start()
			c.join()
	  elif parts[0]=='rmdir':
		if (len(parts)==1) | (len(parts)>2):
                   print("invalid rmdir command")
		else:
			files=parts[1]
			c=threading.Thread(target=commands.rmdir.rmdir,args=(files,))
			c.start()
			c.join()
	  elif parts[0]=='less':
		if (len(parts)==1) | (len(parts)>2):
                   print("invalid command")
		else:
			files=parts[1]
			c=threading.Thread(target=commands.less.less,args=(files,))
			c.start()
			c.join()

	  elif parts[0]=='exit()':
			print "Exiting shell"
			raise SystemExit    
          else:
                print("ERROR: Command not found")
"""
#Main()
"""

if __name__=="__main__":
	number_commands = 0
	while True:
          input()
	  number_commands=number_commands+1
          number_command.append(number_commands)
