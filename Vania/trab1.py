#!/usr/bin/python

def func_max(c, n):
    vMax = c[0]
    i = 0    
    for i in range(n):
        if c[i] > vMax:
            vMax = c[i]
    #print vMax
    return vMax


def sscmax(A, n):
    m = 0
    c = 7 * [0]
    for m in range(n):        
        c[m] = 1
        i = m - 1
    	while i >= 0:            
            tmp = c[i] + 1            
            if (A[i] <= A[m]) and (tmp > c[m]):
                c[m] = c[i] + 1
            i -= 1
    vmax = func_max(c, n)
#    print vmax

def sscmax2(A,n):
    m = 0
    c = 8 * [0]
    for m in range(n):        
        c[m] = 1
        i = m - 1
    	while i >= 0:            
            tmp = c[i] + 1            
            if (A[i] <= A[m]) and (tmp > c[m]):
                c[m] = c[i] + 1
            i -= 1
    vMax = func_max(c, n)    
    k = n
    vSeq = [0] * 8    
    while k >= 0:
        if (c[k] == vMax) and (vSeq[k] == 0):
            vSeq[k] = A[k]
            vMax -= 1
        k -= 1
    print vSeq

sequencia = [5,2,8,6,3,6,9,7]    

sscmax2(sequencia,7)
