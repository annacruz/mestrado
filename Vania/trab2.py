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
    c = [[0]*m]*n
    i = 0
    j = 0   
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = find_max(c[i-1][j],c[i][j-1])
    #print c[n-1][m-1]

def sscml2(X,Y,n,m):
    c = [[0]*8]*8
    i = 0
    j = 0
    vStr = [0]*8
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = find_max(c[i-1][j],c[i][j-1])
    vMax = c[n-1][m-1]
    marca = 1
    k = n - 1
    l = m - 1
    print c
    while vMax >= 0:
        #print vMax
        if c[k][l] == vMax and X[k] == Y[l]:
            vStr[k] = X[k]
            print vStr
            vMax -= 1
            k -= 1
            l -= 1
            print k
        else:
            if marca == 1 and k >= 0:
                marca = 0
                if c[k][l] == c[k-1][l]:
                    k -= 1
                if marca == 0 and l >= 0:
                    marca = 1
                    if c[k][l] == c[k][l-1]:
                        l -= 1
        
    print vStr
sscml2(A,B,6,5)
