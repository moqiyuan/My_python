#! /usr/bin/env python
# -*- coding:utf-8 -*- 

def bubbleSort(l):
    for i in range(len(l)-1):
        flag = True
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                flag = False
        if flag == True:
            break
    return l

if __name__ == '__main__':
    L = [37,13,33,42,21,19,67]
    print(bubbleSort(L))
            

