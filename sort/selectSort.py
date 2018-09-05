#! /usr/bin/env python
# -*- coding= UTF-8 -*-

def selectSort(l):
    for i in range(len(l)-1):
        m = i
        for j in range(i+1,len(l)):
            if l[m] > l[j]:
                m = j
                l[i],l[j]= l[j],l[i]
    return l

if __name__ == '__main__':
    L = [23,44,13,23,9,35,77,86]
    print(selectSort(L))
