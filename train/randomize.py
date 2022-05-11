#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
l=[]
f = open("train_data.txt","r+",encoding="utf-8")
ftr = open("data.train","w+",encoding="utf-8")
fte = open("data.test","w+",encoding="utf-8")
s = f.readlines()
r = list(range(0,len(s)))
l=[str(i) for i in r]
random.shuffle(r)
print(s)
for i in range(0,len(s)):
    l[r[i]]=s[i]
ftr.write("".join(l[:-200]))
fte.write("".join(l[-200:]))
f.close()
ftr.close()
fte.close()
