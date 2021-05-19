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

print(dichotomy_sqrt(34))
