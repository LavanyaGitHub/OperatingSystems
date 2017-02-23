"""@
#Name:chmod
#Description:changes the permissions of the given file
# no permission - 0
#execute - 1
#write - 2
#write and execute - 3
#read - 4
#read and execute - 5
#read and write - 6
#read, write, and execute - 7
#parameters:absolute path of the file
"""
#!/usr/bin/env python
import os
import sys

def chmod(_flag1,_flag2):
	permission=int(_flag1,8)
        print permission
        os.chmod(_flag2,permission)
        print("changed permission of")
        print(_flag2)
