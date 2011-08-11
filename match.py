#!/usr/bin/env python
# coding:utf-8
# author : Dreampuf (soddyque@gmail.com)
# date : 2011-08-11

""" Reverse maximum matching word """


import os
import sys
import time

FILENAME = os.path.join(os.path.curdir, "main.dic")

def main(*args):
    if len(args) < 1:
        print "usage: match.py 南京市长江大桥,结婚的和尚未结婚的,中外科学名著,为人民办公益,费孝通向人大常委会提交书面报告,邓颖超生前使用过的物品"
        return 
    
    tword = args[0].decode("utf-8")[::-1]
    tword_len = len(tword)

    print tword[::-1]

    ts = time.time()
    odic = [i.decode("utf-8").strip()[::-1] for i in open(FILENAME)]
    #print "\n".join(odic[:100])
    odict = [(len(i), i) for i in odic]
    #print "%s" % (time.time() - ts)

    pos = 0
    val = [1 for i in tword]
    cut = [-1]
    while True:
        for n, i in odict:
            if tword[pos] == i[0] and val[pos] <= n and tword[pos:pos+n] == i:
                val[pos:pos+n] = [n]*n
        pos = pos + val[pos]
        if pos >= tword_len:
            break

    val = val[::-1]
    print val
    tword = tword[::-1]
    pos = 0
    while pos < tword_len:
        print tword[pos: pos+val[pos]]
        pos = pos + val[pos]

if __name__ == "__main__":
    main(*sys.argv[1:])
