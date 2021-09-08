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

    # 最长公共子序列
    def lcs_dp(self, input_x, input_y):
        # input_y as column, input_x as row
        dp = [([0] * (len(input_y) + 1)) for i in range(len(input_x) + 1)]
        for i in range(1, len(input_x) + 1):
            for j in range(1, len(input_y) + 1):
                if i == 0 or j == 0:  # 在边界上，自行+1
                    dp[i][j] = 1
                elif input_x[i - 1] == input_y[j - 1]:  # 不在边界上，相等就加一
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # 不相等
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        for dp_line in dp:
            print(dp_line)
        return dp[-1][-1]

    # 最长回文子串
    def lcs3_dp(self, input_x, input_y):
        # input_y as column, input_x as row
        dp = [([0] * (len(input_y) + 1)) for i in range(len(input_x) + 1)]
        maxlen = maxindex = 0
        for i in range(1, len(input_x) + 1):
            for j in range(1, len(input_y) + 1):
                if i == 0 or j == 0:  # 在边界上，自行+1
                    dp[i][j] = 0
                if input_x[i - 1] == input_y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > maxlen:  # 随时更新最长长度和长度开始的位置
                        maxlen = dp[i][j]
                        maxindex = i - maxlen
                        # print('最长公共子串的长度是:%s' % maxlen)
                        # print('最长公共子串是:%s' % input_x[maxindex:maxindex + maxlen])
                else:
                    dp[i][j] = 0
        for dp_line in dp:
            print(dp_line)
        return maxlen, input_x[maxindex:maxindex + maxlen]


if __name__ == '__main__':
    s = Solution()
    values = [1, -2, 3, 10, -4, 7, 2, -5]
    print(s.max_sub_arr(values))
