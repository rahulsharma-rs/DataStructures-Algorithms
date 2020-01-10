"""
This script provides a function to merge two sorted array of different size
input
[ 4 12 14 19 31 33 40 44 46 47]
[ 1  1 24 24 30 31 31 35 37 37 39 46]
output
[1 1 4 12 14 19 24 24 30 31 31 31 33 35 37 37 39 40 44 46 46 47]


"""

import numpy as np
import random
#function to merge two sorted arrays
def merge(arr1=None,arr2=None):

    if arr1.all()==None or arr2.all()==None:
        return -1
    sizeArr1=len(arr1)#Size of first array
    sizeArr2=len(arr2)#Size of second array
    i=0;j=0;k=0#index variable for arr1 arr2 and MergedArray
    MergedArray=np.asarray([None]*(sizeArr1+sizeArr2))#creating an empty array with the size of arr1+arr2
    #loop until one of array is exhausted
    while i<sizeArr1 and j<sizeArr2:
        if arr1[i]<arr2[j]:
            MergedArray[k]=arr1[i]
            k=k+1; i=i+1
        else:
            MergedArray[k]=arr2[j]
            k=k+1; j=j+1
    #if arr1 array is remaining then save it Merged array
    while i<sizeArr1:
        MergedArray[k]=arr1[i]
        i+=1;k+=1
    # if arr2 array is remaining then save it Merged array
    while j<sizeArr2:
        MergedArray[k]=arr2[j]
        j+=1;k+=1
    #returning the merged array
    return MergedArray

arr1=np.sort([random.randint(1,50) for _ in range(10)])#generating first array with 10 elements
arr2=np.sort([random.randint(1,50) for _ in range(12)])#generating first array with 12 elements
print(arr1)
print(arr2)
print(merge(arr1=arr1.copy(),arr2=arr2.copy()))