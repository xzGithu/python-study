#!/usr/bin python

import difflib
import sys

try:
    file1=sys.argv[1]
    file2=sys.argv[2]
except Exception,e:
    print 'error:'+str(e)
    print 'Usage:python ' + sys.argv[0] + ' file1 file2'
    sys.exit()

def readfile(filename):
    try:
        filecon=open(filename,'rb')
        text=filecon.read().splitlines()
        filecon.close()
        return text
    except IOError as error:
        print 'Read file error '+str(error)
        sys.exit()

if file1=="" or file2=="":
    print 'Usage:python ' + sys.argv[0] + ' file1 file2'
    sys.exit()

file1text=readfile(file1)
file2text=readfile(file2)

d=difflib.HtmlDiff()
diffr=d.make_file(file1text,file2text)
print diffr
print d.make_file(file1text,file2text)


