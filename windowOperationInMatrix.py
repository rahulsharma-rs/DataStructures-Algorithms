"""
input
[[ 0,  1,  2,  3,  4],
[ 5,  6,  7,  8,  9],
[10, 11, 12, 13, 14],
[15, 16, 17, 18, 19]]
 output
[[ 0  1  2]
 [ 5  6  7]
 [10 11 12]]
[[ 1  2  3]
 [ 6  7  8]
 [11 12 13]]
[[ 2  3  4]
 [ 7  8  9]
 [12 13 14]]
[[ 5  6  7]
 [10 11 12]
 [15 16 17]]
[[ 6  7  8]
 [11 12 13]
 [16 17 18]]
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
"""

import numpy as np

size_x=4
size_y=5
x1=np.arange(20).reshape((size_x,size_y))

window_x=3#number of rows in the window
window_y=3#number on columns in the window

#looping for number of rows
for x in range(0,4):
    #looping for number of columns in row
    for y in range(0,5):

        if x+window_x-1<size_x and y+window_y-1<size_y:
            #slicing a window of size window_x X window_y for the 2d-matrix x1
            slice=x1[np.ix_([(x+i) for i in range(window_x)]
                            ,[(y+j) for j in range(window_y)])]

            print(slice)