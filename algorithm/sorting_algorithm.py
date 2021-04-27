# 1.冒泡排序
def bubble_sort(list):
    len_list = len(list)
    for i in range(len_list):
        for j in range(1, len_list - i):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    return list


# 2.选择排序
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def select_sort(arr):
    res = []
    while arr:
        s_i = findSmallest(arr)
        res.append(arr.pop(s_i))
    return res


# 3.插入排序
def insert_sort(list):
    len_list = len(list)
    if len_list <= 1:
        return list
    for i in range(1, len_list - 1):
        j = i
        cur = list[j]
        while j > 0 and cur < list[j]:
            list[j] = list[j - 1]
            j -= 1
        list[j] = cur


def InsertSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range(1,n):
        j=i
        target=lst[i]            #每次循环的一个待插入的数
        while j>0 and target<lst[j-1]:       #比较、后移，给target腾位置
            lst[j]=lst[j-1]
            j=j-1
        lst[j]=target            #把target插到空位
    return lst


def quick_sort(nums, left, right):
    if left < right:
        i = left
        j = right
        # 取第一个元素为枢轴量
        pivot = nums[left]
        while i != j:
            while j > i and nums[j] > pivot:
                j -= 1
            if j > i:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] < pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = pivot
        quick_sort(nums, left, i-1)
        quick_sort(nums, i+1, right)
    return nums


if __name__ == '__main__':
    test_list = [4, 2, 1, 3, 7, 8, 5]
    int_list = [int(i) for i in test_list]
    print('冒泡排序：', bubble_sort(test_list))
    print('选择排序：', select_sort(test_list))
    print('插入排序：', InsertSort(int_list))
    print('快速排序：', quick_sort(int_list, 0, 6))
