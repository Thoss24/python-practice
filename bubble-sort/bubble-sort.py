# bubble sort pseudo code

# for i from 1 to n
# for j from 0 to n-1
# if arr[j] > arr[j + 1]
# swap arr[j] with arr[j + 1]

def bubbleSort(arr):
    '''Loop through array'''
    for i in range(len(arr)):
        '''Another loop to compare array elements'''
        for j in range(0, len(arr) - i - 1):
            '''Compare elements next to each other'''
            '''Swap > for < to sort in descending order'''
            if arr[j] > arr[j + 1]:
                '''Swap elements if not in descending order'''
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

array = [1, 4, 2, 8, 5, 9]
            
bubbleSort(array)

print(array)
