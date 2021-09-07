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
