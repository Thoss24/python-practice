import math

def binary(source, target):
   
    firstIndex = 0
    lastIndex = len(source) - 1
    mid = 0

    while (firstIndex <= lastIndex):
        '''Find middle of array'''
        mid = (firstIndex + lastIndex) // 2
        '''If middle value is less than target, target can only be present in right half of array. So we set firstIndex to equal first index in right half'''
        if source[mid] < target:
            firstIndex = mid + 1
            '''If middle value is greater than target, target can only be present in left half of array. So we set last index to be the last index in left half of array'''
        elif source[mid] > target:
            lastIndex = mid - 1
            '''Else return middle value as middle an target are equal by default'''
        else:
            return mid
        '''If value doesn't exist return -1'''
    return -1



arr = [2, 3, 4, 10, 40]
x = 3
result = binary(arr, x)

if result != -1:
    print(str(result))
else:
    print("Not found")