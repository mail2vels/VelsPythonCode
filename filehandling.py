print '''
2. Write a program which will read a file from given path, calculate the size of the file and write it to another file.
   Also append timestamp, if the size of the file is greater than 1 MB then throw an error. Implement using try catch. 
'''

filename = raw_input('Provide the File Name / Path: ')
print 'File Path : ' + str(filename) + '\n'

fh = open(filename, 'r')
filecontents = fh.read()
#print "\nShow file contents Below"
#print "==========================\n"
#print filecontents

import os

print "Option 1: Using Os Path"

filesize = os.path.getsize(filename)
print 'The File Size is = ' + str(filesize)

print "Option 2: Using OS Stat"
filesize = os.stat(filename)
print 'The File Size is = ' + str(filesize.st_size)

from stat import *
st = os.stat(filename)
#print st[ST_SIZE]

fsmb = (st[ST_SIZE]/1024)/1024

#print (fsmb)

if(fsmb >= 1):
	print 'File Size Greater than 1 MB'
else:
    print 'File Size is Lesser than 1 MB'

fh = open('filesize_finder.txt', 'a')

import datetime
DateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
contentToWrite = "File Name = " + filename + ", File Size = " + str(filesize.st_size)+ " Bytes,  In MB = " + str(fsmb) + ", File Size Calculated On = " + str(DateTime) + "\n"
fh.writelines(contentToWrite)

fh.close()






