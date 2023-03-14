from random import randint
from timeit import repeat

# quicksort pseudo code

'''Function to find partition position'''
def partition(arr, low, high):

    '''Select rightmost element as pivot'''
    pivot = arr[high]

    '''Pointer for greater element'''
    i = low - 1

    '''Loop through each element'''
    '''Compare each element with pivot'''
    for j in range(low, high):
        if arr[j] <= pivot:
            '''If element smaller than pivot is found swap it with the greater element pointed by i'''
            i = i + 1

            '''Swap element at i with element at j'''
            (arr[i], arr[j]) = (arr[j], arr[i])

        '''Swap the pivot element with the greater element specified by i'''
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

        '''Return position from where the partition is done'''
        return i + 1


def quickSort(arr, low, high):
    if low < high:

        '''Find pivot element as follows:'''
        '''Elements smaller than pivot are on the left'''
        '''Elements greater than pivot are on the right'''
        pi = partition(arr, low, high)

        '''Recursive call on left of pivot'''
        quickSort(arr, low, pi - 1)

        '''Recursive call on right of pivot'''
        quickSort(arr, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]

size = len(data)

quickSort(data, 0, size - 1)

print(data)


# average time complexity O(N log N)