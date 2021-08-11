# coins 凑零钱
def add_coins(origin_list, amount):
    dp = [amount+1]*(amount+1)
    print(dp)
    # dp[i]表示凑出i元，最少需要的硬币个数
    dp[0] = 0
    for i in range(len(dp)):
        for coin in origin_list:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1+dp[i-coin])
    if dp[amount] == amount+1:
        return -1
    else:
        return dp[amount]

print(add_coins([1,2,5],  8))

class Solution:
    # 股票买卖问题，只能在某一天买入，在未来的某一天卖出
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        for i in range(n):
            # 表示当天没有持有股票，两种情况：1.前一天也没有；2前一天有今天卖出去
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            # 表示当天持有，两种情况：1.前一天已经持有；2前一天没有今天打算买入
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

    # 假设可以进行K次交易
    def maxProfit(self, prices) -> int:
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0


