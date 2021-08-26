# max sub array sum
def max_sub_arr(list):
    list_len = len(list)
    if list_len == 0:
        return
    if list_len == 1:
        return list[0]
    dp = [False for _ in range(list_len)]
    dp[0] = list[0]
    for i in range(1, list_len):
        dp[i] = max(dp[i-1]+list[i], list[i])
    return max(dp)


# max multi
def max_product(nums):
    n = len(nums)
    dp_max = [nums[0]] * n
    dp_min = [nums[0]] * n
    res = nums[0]
    for i in range(1, n):
        dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
        dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
        res = max(res, dp_max[i])
    return res


if __name__ == '__main__':
    values = [1, -2, 3, 10, -4, 7, 2, -5]
    print(max_sub_arr(values))