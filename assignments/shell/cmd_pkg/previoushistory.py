def previoushistory(file):
	x1=[]
	y=[]
	x1=list(file)
	del x1[0]
	files=''.join(x1)
	l=len(command_history)
	for i in range(l):
		if (command_new[i]==files):
			index=i
	cmd1 = command_history[index]
	print cmd1
	y=cmd1.split(" ")
	print y[0]
	length= len(y)
	file1=eval(y[0])

	if length==1:
		print "in if"
	#	file1=getattr(y[0])
		t=threading.Thread(target=file1)
		t.start()
		t.join()
	elif length==2:
		file2=y[1]
		print file2
		t=threading.Thread(target=file1,args=(file2,))
		t.start()
		t.join()
	elif length==3:
		file2=y[1]
		file3=y[2] 
		t=threading.Thread(target=file1,args=(file2,file1,))
                t.start()
                t.join()
	elif length==4:
		file2=y[1]
                file3=y[2]
		file4=y[3]
		t.threading.Thread(target=file1,args=(file2,file3,file4,))
		t.start()
		t.join()
