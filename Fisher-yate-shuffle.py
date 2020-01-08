import numpy as np
from random import randrange
'''method to perform inplace shuffling inspired by Fisher–Yates shuffle algorithm '''
def fisherYateShuffle(item=None):
    #condition to check an empty of None array
    if item.dtype =='int64' or item.dtype =='float64':
        if item.all()==None or len(item)==0:
            return -1
    else:
        if len(item)==0:
            return -1
    #assign length of the array
    length=len(item)
    for i in range(0,length):
        if i!=length-1:
            #if i index is not the the last index
            j=randrange(i,length)
        else:
            i=j
        #swap i and j indexes of the array
        item[j],item[i]=item[i],item[j]
    return item

if __name__=='__main__':
    #numeric array
    #arr=np.asarray([1,2,3,4,5,6])
    #character array
    arr=np.asarray(['a','b','c','d','e','f','g'])
    print(fisherYateShuffle(item=arr.copy()))
    print(fisherYateShuffle(item=arr.copy()))
    print(fisherYateShuffle(item=arr.copy()))
    print(fisherYateShuffle(item=arr.copy()))
    print(fisherYateShuffle(item=arr.copy()))
    print(fisherYateShuffle(item=arr.copy()))


