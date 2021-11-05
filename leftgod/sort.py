# select sort
# 时间复杂度O(n2)，空间复杂度O(1)
def select_sort(arr):
    if not arr or len(arr) < 2:
        return arr
    min_index = 0
    for i in range(len(arr)-1):
        print(arr)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        print(i,min_index)
        swap(arr, i, min_index)
    return arr


def bubble_sort(arr):
    if not arr or len(arr) < 2:
        return arr
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)
    return arr


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


li = [89,13,32,12,1,3,9,0]
# print(select_sort(li))
print(bubble_sort(li))