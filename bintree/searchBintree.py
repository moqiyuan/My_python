# -*- coding: UTF-8 -*-

#Search
def searchBintree(tree,num):
    if tree == []:
        return False
    if num == tree[0]:
        return True
    if num < tree[0]:
        return searchBintree(tree[1],num)
    if num > tree[0]:
        return searchBintree(tree[2],num)

mytree = [56,
    [32,[27,[],[]],[]],
    [77,
        [74,[60,[],[]],[]],
        []]]
if searchBintree(mytree,60):
    print('Yes')
else:
    print('No')