
def quick_sort(input_list, start, end):
    if start >= end:
        return input_list
    pivot = input_list[start]
    i = start
    j = end
    while i < j:
        while i < j and input_list[j] >= pivot:
            j -= 1
        input_list[i] = input_list[j]
        while i < j and input_list[i] < pivot:
            i += 1
        input_list[j] = input_list[i]
    input_list[i] = pivot
    quick_sort(input_list, start, i - 1)
    quick_sort(input_list, i + 1, end)
    return input_list


if __name__ == '__main__':
    in_list = [3, 5, 6, 2, 1, 4]
    res = quick_sort(in_list, 0, len(in_list) - 1)
    print(res)