#__Author__: 42902
#__Date__: 2019/2/28
def binary_search(array,val):
    beg=0
    end=len(array)-1
    while True:
        mid=int((beg+end)/2)
        if array[mid]==val:
            return mid
        elif array[mid]>val:
            end=mid-1
        else:
            beg=mid+1
    return -1


print(binary_search([1,2,3,4,5],5))