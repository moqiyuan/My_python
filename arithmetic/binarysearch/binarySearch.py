# -*- coding = UTF-8 -*-


def BinarySearch(l, n):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] < n:
            low = mid + 1
        elif l[mid] > n:
            high = mid - 1
        else:
            return mid, l[mid]
    return None


# sorted array
L = [3, 4, 7, 11, 13, 17, 20, 108]
print(BinarySearch(L, 3))
print(BinarySearch(L, 99))
print(BinarySearch(L, 13))