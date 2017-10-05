# -*- coding: utf-8 -*-
n,p,h = 0,0,0
while True:
    n = n+1
    #print(n)
    tri = n*(n+1)/2
    for i in range(n):
        pent = i*((3*i) - 1)/2
        if(pent > tri):
            break
        if(pent == tri):
            p = pent
            break
    for j in range(n):
        hexa = j*((2*j) - 1)
        if(hexa > tri):
            break
        if(hexa == tri):
            h = hexa
            break
    if(tri == p == h):
        print("###################################################################")
        print(tri)
        print("###################################################################")
        break
