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


if __name__ == "__main__":
    in_list = [34, 12, 23, 15, 45, 18, 66, 17, 10, 77]
    quick_sort(in_list, 0, len(in_list) - 1)
    print(in_list)