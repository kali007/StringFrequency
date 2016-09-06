#coding=utf-8


import os
import sys
from os.path import join
from operator import itemgetter

def isexit (i,line,j,e):
    
    if e.has_key(line[i:j]):
        c=e[line[i:j]]+1
        e[line[i:j]]=c
    else:
        e[line[i:j]]=1
    return e
    
def tj(path,list):            
    e={}
    for line in open(path):
        e=isexit(0,line,40,e)
    for k in e.keys():
        if e[k]<10000:
            del(e[k])
    d=sorted(e.iteritems(), key=itemgetter(1), reverse=True)
    for i in range(0,len(d)):
        list.append(d[i])
 #   for c in d:
 #       print c
        
def main() :
    dest = sys.argv[1]
    list=[]
    for root, dirs, files in os.walk(dest):
        for OneFileName in files :
            if OneFileName.find( '.txt' ) == -1 :
                continue
            OneFullFileName = join( root, OneFileName )
            tj(OneFullFileName,list)
            print OneFullFileName
    list=sorted(list, key=itemgetter(1), reverse=True)
    file = open('list.txt','a+')
    for c in list:
        print c
        file.write(str(c) + '\n')
    file.close
                
if __name__ == "__main__" :
    main()



