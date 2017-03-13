"""@
#Name:wc
#Description:counts the number of words in a given file
#parameters: file
"""
import threading
import os
import sys

def wc(file):
        if(os.path.isfile(file)):
            num_lines = 0
            num_words = 0
            num_chars = 0
            with open(file, 'r') as f:
                for line in f:
                    words = line.split()
                    num_lines += 1
                    num_words += len(words)
                    num_chars += len(line)
		print("number of line:"),
                print(num_lines)
		print("number of words:"),
                print(num_words)
		print("number of characters:"),
                print(num_chars)
		print("filename:"),
		print(file)
        else:
            print("file does not exist")