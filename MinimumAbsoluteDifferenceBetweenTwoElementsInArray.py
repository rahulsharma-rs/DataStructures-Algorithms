"""
input
[-70 -33 -96   3 -46  78  72  73 -86   8  56  12   5  -6  66  31 -81   5 -40 -52]
output
0

the problem is solved by applying Greedy approach
"""


import numpy as np
import random

def findMinDif(arr=None):
    if arr.all()==None:
        return -1
    #sorting the array in assending order
    arr=np.sort(arr)
    #defining a very large differnce value
    dif=100**20
    print(arr)
    #iterating to find the minimum difference among the alemens
    for i in range(len(arr)-1):

        if arr[i+1] - arr[i]<dif:
            dif=arr[i+1] - arr[i]
    return dif

#create an array of random integers
RandomArraytOfIntegers = np.asarray([random.randint(-100, 100) for iter in range(20)])
print(RandomArraytOfIntegers)
print(findMinDif(RandomArraytOfIntegers.copy()))
