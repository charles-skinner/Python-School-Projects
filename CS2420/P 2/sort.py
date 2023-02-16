import time
from random import seed, sample

"""
this is a docstring
"""

def quicksort(lyst):
    """
    this is a docstring
    """
    return quicksorter(lyst,0,len(lyst)-1)


def quicksorter(lyst,left,right):
    """
    this is a docstring
    """
    if left == right:
        return lyst
    if left < right:
        split = partition(lyst,left,right)
        quicksorter(lyst,left,split-1)
        quicksorter(lyst,split+1,right)
    return lyst
    

def partition(lyst,i,j):
    """
    this is a docstring
    """
    pivot = lyst[i]
    while i < j:
        while lyst[i] < pivot:
            i += 1
        while lyst[j] > pivot:
            j -= 1
        lyst[i], lyst[j] = lyst[j], lyst[i]
    return j
    

def mergesort(lyst):
    """
    this is a docstring
    """
    length = len(lyst)
    if length <= 1:
        return lyst
    left = []
    right = []
    for i in range(length):
        if i < length/2:
            left.append(lyst[i])
        else:
            right.append(lyst[i])
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right)


def merge(apple,banana):
    """
    this is a docstring
    """
    chicken = []
    while apple and banana:
        if apple[0] < banana[0]:
            chicken.append(apple[0])
            apple.remove(apple[0])
        else:
            chicken.append(banana[0])
            banana.remove(banana[0])
    while apple:
        chicken.append(apple[0])
        apple.remove(apple[0])
    while banana:
        chicken.append(banana[0])
        banana.remove(banana[0])
    return chicken


def selection_sort(lyst):
    """
    this is a docstring
    """
    sorted_lyst = []
    while lyst:
        min = findmin(lyst)
        sorted_lyst.append(lyst[min])
        del lyst[min]
    return sorted_lyst


def findmin(lyst):
    """
    this is a docstring
    """
    min = 0
    for i in range(len(lyst)):
        if lyst[i] < lyst[min]:
            min = i
    return min


def insertion_sort(lyst):
    """
    this is a docstring
    """
    for i in range(1,len(lyst)):
        if lyst[i] < lyst[i-1]:
            value = lyst[i]
            del lyst[i]
            for j in range(0,i):
                if value < lyst[j]:
                    lyst.insert(j,value)
                    break

    return lyst


def is_sorted(lyst):
    """
    this is a docstring
    """
    for i in range(len(lyst)):
        if isinstance(lyst[i],int) is False:
            return False
    return lyst == sorted(lyst)


def main():
    """
    this is a docstring
    """
    data_size = 6
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    test = sorted(data.copy())

    start = time.perf_counter()
    result = quicksort(data.copy())
    tyme = time.perf_counter() - start
    print(f"quicksort ran {test == result}, duration = {tyme}")

    start = time.perf_counter()
    result = mergesort(data.copy())
    tyme = time.perf_counter() - start
    print(f"mergesort ran {test == result}, duration = {tyme}")

    start = time.perf_counter()
    result = selection_sort(data.copy())
    tyme = time.perf_counter() - start
    print(f"selection_sort ran {test == result}, duration = {tyme}")

    start = time.perf_counter()
    result = insertion_sort(data.copy())
    tyme = time.perf_counter() - start
    print(f"insertion_sort ran {test == result}, duration = {tyme}")

    start = time.perf_counter()
    result = is_sorted(data.copy())
    tyme = time.perf_counter() - start
    print(f"is_sorted ran {result}, duration = {tyme}")


if __name__ == "__main__":
    main()