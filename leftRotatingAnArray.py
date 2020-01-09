"""
input
[0 1 2 3 4 5 6 7 8 9]
output
[1 2 3 4 5 6 7 8 9 0]-->after first left rotation
[2 3 4 5 6 7 8 9 0 1]-->after second left rotation
"""

import numpy as np


def rotate(arr=None):
    if arr.all()==None:
        return -1
    length=len(arr)
    temp=arr[0]
    for i in range(length-1):
        arr[i]=arr[i+1]
    arr[length-1]=temp
    return arr
arr= np.arange(10)

print(arr)
arr=rotate(arr=arr.copy())
print(arr)
arr=rotate(arr=arr.copy())
print(arr)