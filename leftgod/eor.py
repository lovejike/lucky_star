# 1.异或运算，可用于计算只出现一次的数据
# 特性：N^0=N,N^N=0
def appear_only_once(arr):
    eor = 0
    for i in arr:
        eor = eor ^ i
    return eor


# 2. 找出数组中出现了奇数次的两个数字
def appear_twice(arr):
    # Step1. 整体异或一遍，得到eor=a^b
    eor = 0
    for aa in arr:
        eor ^= aa
    # Step2. eor肯定不等于0，至少有一位上是1，此步骤找到eor最右边的1
    right_one = eor & (~eor + 1)
    # Step3. 找到a或者b
    first = 0
    for ele in arr:
        # 找出最右为1的位置上是0的全部数据进行异或，得到a/b
        if ele & right_one == 0:
            first ^= ele
    return first,  first ^ eor
    # print(first, " ", first ^ eor)

list = [1,3,3,99,9,99,9,88,1,2]
# print(appear_only_once(list))
print(appear_twice(list))