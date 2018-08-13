# -*- coding: UTF-8 -*-

#Insert
def insertBintree(tree,num):
    if tree == []:
        tree.extend([num,[],[]])
    elif num <= tree[0]:
        insertBintree(tree[1],num)
    elif num > tree[0]:
        insertBintree(tree[2],num)
    return tree


mytree = [56,
    [32,[27,[],[]],[46,[],[]]],
    [77,
        [74,[60,[],[]],[]],
        [108,[],[]]]]
print(insertBintree(mytree,70))