def maxSubArray(self, nums):
    size = len(nums)
    if size == 0:
        return None
    if size == 1:
        return nums[0]

    dp = [False for _ in range(size)]  # 记录状态：当前以i结尾的最大值记录在里面
    dp[0] = nums[0]

    for i in range(1, size):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 记录最大状态
    return max(dp)


if __name__== '__main__':
    values = [1, -2, 3, 10, -4, 7, 2, -5]
    print(maxSubArray(values))