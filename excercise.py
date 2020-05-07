# !/usr/bin/env python
my_list=[1,23,45,'hello','43',-23,'-56','one',5.6]
anotherList=[]
for i in my_list:
    try:
        if i!=float(i):
            i=int(i)
        if i==int(i):
            anotherList.append(i)
    except:
        print()


print([i for i in anotherList])

