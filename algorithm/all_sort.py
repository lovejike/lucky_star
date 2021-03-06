def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid = len(input_list) // 2
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])
    return merge(left, right)


def merge(start, end):
    i = 0
    j = 0
    res = []
    while i < len(start) and j < len(end):
        if start[i] <= end[j]:
            res.append(start[i])
            i += 1
        else:
            res.append(end[j])
            j += 1
    res += start[i:]
    res += end[j:]
    return res


def quick_sort(input_list, start, end):
    if start >= end:
        return
    mid = input_list[start]
    low = start
    high = end
    while low < high:
        while low < high and input_list[high] >= mid:
            high -= 1
        input_list[low] = input_list[high]
        while low < high and input_list[low] < mid:
            low += 1
        input_list[high] = input_list[low]
    input_list[low] = mid
    quick_sort(input_list, start, low - 1)
    quick_sort(input_list, low + 1, end)


def part(arr, low, high):
    i = low - 1
    pivot = arr[high]
    print(low)
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i +1]
    return (i+1)


def qs(arr, low, high):
    if low < high:
        p = part(arr, low, high)
        qs(arr, low, p-1)
        qs(arr, p+1, high)
    return arr


if __name__ == "__main__":
    in_list = [34, 12, 23, 15, 45, 18, 66, 17, 10, 77]
    #quick_sort(in_list, 0, len(in_list) - 1)
    print(in_list)
    #print(merge_sort(in_list))
    print(qs(in_list, 0, 9))