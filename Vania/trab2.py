#!/usr/bin/python

A = [1, 2, 3, 2, 4, 1, 2]
B = [2, 4, 3, 1, 2, 1]
#resultado esperado: 2,3,2,1

def find_max(a,b):
    mVal = a
    if a < b:
       mVal = b
    return mVal

def sscml(X, Y, n, m):
    c = [[0]*n]*m    
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = find_max(c[i-1][j],c[i][j-1]
    return c

sscml(A,B,6,5)
