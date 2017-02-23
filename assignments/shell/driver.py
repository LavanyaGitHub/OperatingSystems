"""
Report: 
Project Title: Shell Implementation
Date : 02/ 23/ 2017
Group :         1.Keerthi Reddy Gangidi
		2.Lavanya Mengaraboina
		3.Shaila Mogalapu
Commands Implemented: 
1. ls                           8.  rm                     15. wc                      22.!x
2. ls -l                        9.  rmdir                  16. command1 | command2
3. mkdir                        10. cat                    17. cat file1 file2 > file0
4. cd (directory, ~, ..)        11. less                   18. sort
5. pwd                          12. head                   19. who
6. cp                           13. tail                   20. history
7. mv                           14. grep                   21. chmod
Commands not working:
1. ls -a(cannot display hidden files)
2. command > file ()
Unimplemented Commands:
1. cmd >> file
2. cmd < file
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
"""
#description: displays all the commands that were executed
"""
def history():
		new=list(enumerate(command_history))
		for i,v in enumerate(command_history,start=0):
			print i,v
			#print '\n' .join(command_history)
	
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
		print "back"
		
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

def previoushistory(cmd):
#	print "in prev"
	x1=[]
	y=[]
	x1=list(cmd)
	del x1[0]
	files=''.join(x1)
	files=eval(files)
	new=list(enumerate(command_history))
	# print new
	y=new[files]
	newcmd= y[1].strip(" ")
	runshell(newcmd)
"""
specifies redirect and the pipe commands their functionality according to the given input
"""
def input():
	 cmd = raw_input("%" )
	 p=[]
	 c=[]
	 c1=[]
	 runshell(cmd)
	 # print len(c)
	 
"""
Invoking all the defined commands using threading
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
	  if '>' in cmd:
                if(len(c)==3):
                        p=cmd.split(">")
			p[0]=p[0].strip(" ")
                        t=threading.Thread(target=redirect,args=(c[0],c[2],))
                        t.start()
                        t.join()
                elif(len(c)==4):
                        p=cmd.split(">")
                        p[0]=p[0].strip(" ")
                        print p[0]
                        t=threading.Thread(target=redirect,args=(p[0],c[3],))
                        t.start()
                        t.join()
                elif(len(c)==5):
                        # print "in if 5"
                        p=cmd.split(">")
                        p[0]=p[0].strip(" ")
                        c=threading.Thread(target=redirect,args=(p[0],c[4],))
			c.start()
			c.join()
		elif(len(c)!=5):
			runshell(cmd)
	  elif '|' in cmd:
		 c=cmd.split("|")
		 c[0]=c[0].strip(" ")
		 c[1]=c[1].strip(" ")
		 file1=str(c[0])
		 file2=str(c[1])
		 t=threading.Thread(target=piping,args=(file1,file2,))
		 t.start()
		 t.join()
	 # else: 
		# runshell(cmd)
	  elif parts[0]=='rm':
                if(len(parts)==1) | (len(parts)>2):
                  print("invalid rm command")
                elif(len(parts)==2):
                   files=parts[1]
		   c=threading.Thread(target=commands.rm.rm,args=(files,))
		   c.start()
		   c.join()
	  elif parts[0] == 'pwd':
			c = threading.Thread(target=commands.pwd.pwd)
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
		     c=threading.Thread(target=commands.grep.grep,args=(parts[2],parts[1],))
		     c.start()
		     c.join()
	  elif '!' in cmd:
		     c=threading.Thread(target=previoushistory,args=(parts[0],))
		     c.start()
		     c.join()
	  elif parts[0]=='ls':
                if(len(parts)==1):
                    c=threading.Thread(target=commands.ls.ls)
		    c.start()
		    c.join()
                elif (len(parts)==2):
		    files=parts[1]
                    c=threading.Thread(target=commands.lsfun.lsfun,args=(files,))
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
                   print("invalid cd command")
                elif(len(parts)==2):
                    files=parts[1]
		    c=threading.Thread(target=commands.cd.cd,args=(files,))
		    c.start()
		    c.join()
	  elif parts[0] == 'cat':
		print "in cat"
		print len(parts)
		if (len(parts)==2):
			file = parts[1]
			c = threading.Thread(target=commands.cat.cat, args=(file,))
			c.start()
			c.join()
		elif (len(parts)==5):
		 print "in len"
		 file1=parts[1]
		 file2=parts[2]
		 file3=parts[4]
		 c=threading.Thread(target=commands.cat1.cat1,args=(file1,file2,file3,))
		 c.start()
		 c.join()
	  
          elif parts[0] == 'chmod':
			flag1 = parts[1]
			flag2 = parts[2]
			c = threading.Thread(target=commands.chmod.chmod, args=(flag1, flag2,))
			c.start()
			c.join()			
	  elif parts[0] == 'cp':
			file1 =parts[1]
			file2 = parts[2]
			c = threading.Thread(target=commands.cp.cp, args=(file1,file2,))
			c.start()
			c.join()
	  elif parts[0]=='wc':
                if(len(parts)==1) | (len(parts)>2):
                  print("invalid wc command")
                elif(len(parts)==2):
		    files=parts[1]
		    c=threading.Thread(target=commands.wc.wc,args=(files,))
                    c.start()
		    c.join()
	  elif parts[0]=='sort':
		files=parts[1]
		c=threading.Thread(target=commands.sort.sort,args=(files,))
		c.start()
		c.join()
	  elif parts[0]=='head':
		files=parts[1]
		c=threading.Thread(target=commands.head.head,args=(files,))
		c.start()
		c.join()
	  elif parts[0] == 'mkdir':
			files = parts[1]
			c = threading.Thread(target=commands.mkdir.mkdir,args=(files,))
			c.start()
			c.join()
	  elif parts[0]=='rmdir':
		files=parts[1]
		c=threading.Thread(target=commands.rmdir.rmdir,args=(files,))
		c.start()
		c.join()
	  elif parts[0]=='less':
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
Main()
"""

if __name__=="__main__":
	number_commands = 0
	while True:
          input()
	  number_commands=number_commands+1
          number_command.append(number_commands)
