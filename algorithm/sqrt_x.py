def dichotomy_sqrt(x):
    index = -1
    low = 0
    high = x
    while low <= high:
        mid = (low + high)//2
        if mid * mid < x:
            index = mid
            low = mid + 1
        else:
            high = mid - 1

    return index


def largest_perimeter(list):
    if not list:
        return 0
    if len(list) < 3:
        return 0
    sorted(list)
    i = len(list) - 1
    while i >= 2:
        if list[i] < list[i-1] + list[i-2]:
            return list[i-1] + list[i-2] + list[i]
        else:
            i -= 1
    return 0


if __name__ == "__main__":
    print(dichotomy_sqrt(34))
    list = [3, 2, 3, 6]
    print(largest_perimeter(list))
