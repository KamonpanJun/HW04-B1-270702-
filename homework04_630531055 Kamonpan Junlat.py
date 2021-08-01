# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:37:02 2021

@author: Lenovo
"""

def largestNumber(A):
    maxlen = len(str(max(A)))
    if all(v == 0 for v in A):
        return '0'
    return ''.join(sorted((str(v) for v in A), reverse=True,
                      key=lambda i: i*(maxlen * 2 // len(i))))

X = largestNumber(list(int(X) for X in input("Enter non negative integers in your list:").split()))
print ("the largest formed number is", X)

