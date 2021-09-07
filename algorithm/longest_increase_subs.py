class Solution:
    # 最长上升子序列（非连续）
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    # 最长上升子序列（连续）
    def findLengthOfLCIS(self, nums) -> int:
        n = len(nums)
        # 初始化
        dp = [1] * n
        if not nums:
            return 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


    # 子数组最大和
    def max_sub_arr(self, list):
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


    # 子数组最大乘积
    def max_product(self, nums):
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
    s = Solution()
    values = [1, -2, 3, 10, -4, 7, 2, -5]
    print(s.max_sub_arr(values))
