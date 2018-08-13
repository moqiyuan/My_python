# -*- coding: UTF-8 -*-

def getmax(tree):
    if tree[2] == []:
        max_x = tree[0]
        if tree[1] != []:
            tree[:] =tree[1]
        else:
            tree.clear()
        return max_x
    else:
        return getmax(tree[2])

#Delete
def deleteBintree(tree,num):
    if tree == []:
        return False
    if num < tree[0]:
        return deleteBintree(tree[1],num)
    elif num > tree[0]:
        return deleteBintree(tree[2],num)
    else:
        if tree[1] == [] and tree[2] == []:
            tree.clear()
        elif tree[1] == []:
            tree[:] = tree[2]
        elif tree[2] == []:
            tree[:] = tree[1]
        else:
            max_l = getmax(tree[1])
            tree[0] = max_l
        return tree


mytree = [56,
    [32,[27,[],[]],[46,[],[]]],
    [77,
        [74,[60,[],[]],[]],
        [108,[],[]]]]
print(mytree)
print(deleteBintree(mytree,32))