#__Author__: 42902
#__Date__: 2019/2/28

#https://www.bilibili.com/video/av26524633?t=112

import sys
sys.setrecursionlimit(100000) #设置递归深度为一百万

def quickSort(array):
    if len(array)<2:
        return array
    else:
        pivot_index=0
        pivot=array[pivot_index]
        less_part=[i for i in array[pivot_index+1:] if i<=pivot]
        great_part=[i for i in array[pivot_index+1:] if i>pivot]
        return quickSort(less_part)+[pivot]+quickSort(great_part)

def partition(array,beg,end):
    pivot_idnex=beg
    pivot=array[pivot_idnex]
    left=pivot_idnex+1
    right=end-1
    while True:
        while left<=right and array[left]<pivot:
            left+=1
        while right>=left and array[right]>=pivot:
            right-=1
        if left>right:
            break
        else:
            array[left],array[right]=array[right],array[left]
    array[pivot_idnex],array[right]=array[right],array[pivot_idnex]
    return right
def quickSort_inplace(array,beg,end):
    if beg<end:
        pivot_index=partition(array,0,len(array))
        quickSort_inplace(array,beg,pivot_index)
        quickSort_inplace(array,pivot_index+1,end)



l=[2,8,4,9,5]
quickSort_inplace(l,0,len(l))
print(l)