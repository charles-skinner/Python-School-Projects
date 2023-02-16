import time
from random import seed, sample
from time import perf_counter
from math import sqrt

"""
this is project 1
"""

def linear_search(lyst, target):
    """
    searches lyst for target, returns true or false
    """
    for i in range(len(lyst)):
        if lyst[i] == target:
            return True
    return False


def binary_search(lyst, target):
    """
    searches lyst for target, returns true or false
    """
    low = 0
    mid = 0
    high = len(lyst)-1
    while high >= low:
        mid = (high + low) // 2
        if lyst[mid] < target:
            low = mid + 1
        elif lyst[mid] > target:
            high = mid - 1
        else:
            return True
    return False


def jump_search(lyst, target):
    """
    searches lyst for target, returns true or false
    """
    i = 0
    n = len(lyst)
    m = int(sqrt(n))
    while (i < n) and (lyst[i] <= target):
        if i > n:
            return False
        i += m
    for j in range(i-m,i):
        if lyst[j] == target:
            return True
    return False


def main():
    #create data to use on all the searches
    data_size = 1000000
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()

    #run binary search for last item and print results
    start = time.perf_counter()
    result = binary_search(data, data[-1])
    tyme = time.perf_counter() - start
    print(f"binary search ran for last item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run linear search for last item and print results
    start = time.perf_counter()
    result = linear_search(data, data[-1])
    tyme = time.perf_counter() - start
    print(f"linear search ran for last item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run jump search for last item and print results
    start = time.perf_counter()
    result = jump_search(data, data[-1])
    tyme = time.perf_counter() - start
    print(f"jump search ran for last item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run linear search for first item and print results
    start = time.perf_counter()
    result = linear_search(data, data[0])
    tyme = time.perf_counter() - start
    print(f"linear search ran for first item\n\tresult = {result}\n\ttime = {tyme} sec")
    
    #run binary search for first item and print results
    start = time.perf_counter()
    result = binary_search(data, data[0])
    tyme = time.perf_counter() - start
    print(f"binary search ran for first item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run jump search for first item and print results
    start = time.perf_counter()
    result = jump_search(data, data[0])
    tyme = time.perf_counter() - start
    print(f"jump search ran for first item\n\tresult = {result}\n\ttime = {tyme} sec")
    
    #run linear search for middle item and print results
    start = time.perf_counter()
    result = linear_search(data, data[(data_size // 2) - 1])
    tyme = time.perf_counter() - start
    print(f"linear search ran for middle item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run binary search for middle item and print results
    start = time.perf_counter()
    result = binary_search(data, data[(data_size // 2) - 1])
    tyme = time.perf_counter() - start
    print(f"binary search ran for middle item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run jump search for middle item and print results
    start = time.perf_counter()
    result = jump_search(data, data[(data_size // 2) - 1])
    tyme = time.perf_counter() - start
    print(f"jump search ran for middle item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run linear search for unfindable item and print results
    start = time.perf_counter()
    result = linear_search(data, data_size * 4)
    tyme = time.perf_counter() - start
    print(f"linear search ran for unfindable item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run binary search for unfindable item and print results
    start = time.perf_counter()
    result = binary_search(data, data_size * 4)
    tyme = time.perf_counter() - start
    print(f"binary search ran for unfindable item\n\tresult = {result}\n\ttime = {tyme} sec")

    #run jump search for unfindable item and print results
    start = time.perf_counter()
    result = jump_search(data, data_size * 4)
    tyme = time.perf_counter() - start
    print(f"jump search ran for unfindable item\n\tresult = {result}\n\ttime = {tyme} sec")


if __name__ == "__main__":
    main()
    