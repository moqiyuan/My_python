# -*- coding: UTF-8 -*-


def prime_Factor(n):
    n = int(n)
    for i in range(2, n//2+1):
        if n % i == 0:
            l.append(i)
            return prime_Factor(n/i)
    l.append(n)
    return l


if __name__ == "__main__":
    n = input('please input a number:')
    l = []
    L = prime_Factor(n)
    st = str(n)+'='
    for i in L:
        st = st + str(i) + 'x'
    print(st[:-1])