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


