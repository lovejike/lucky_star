# 计算子数组的最大和
def max_sum_func(in_list):
    max_sum = 0
    cur_sum = 0
    if in_list is None:
        return max_sum

    for value in in_list:
        cur_sum += value
        if cur_sum < 0:
            cur_sum = 0
        if cur_sum > max_sum:
            max_sum = cur_sum

    if max_sum == 0:
        max_sum = in_list[0]
        for i in in_list[1:]:
            if i > max_sum:
                max_sum = i

    return max_sum


if __name__== '__main__':
    values = [1, -2, 3, 10, -4, 7, 2, -5]
    print(max_sum_func(values))