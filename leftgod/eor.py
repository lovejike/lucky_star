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

# 1. 二分查找
def binary_search_exist(sort_arr, num):
    n = len(sort_arr)
    if not sort_arr or n < 1:
        return False
    L, R = 0, n-1
    mid = 0
    print("0")
    while L < R:
        print(L, R)
        mid = L + ((R-L) >> 1)
        print(mid)
        if sort_arr[mid] == num:
            return True
        elif sort_arr[mid] > num:
            R = mid-1
        else:
            L = mid+1
    return sort_arr[L] == num


# 2. 只有一种数出现了奇数次，其余偶数次
def once(arr):
    eor = 0
    for i in arr:
        eor ^= i
    return eor


# 3.提取整形数，最后侧的1
def most_right(num):
    return num & (~num + 1)


# 4. 数组中有两种数字出现了奇数次，其余出现了偶数次，返回这两个数
def two_once(arr):
    eor = 0
    n = len(arr)
    for i in range(n):
        eor ^= arr[i]
    mr = most_right(eor)
    one_of = 0
    for i in range(n):
        if mr & arr[i] != 0:
            one_of ^= arr[i]
    return one_of, eor^one_of


# 5.返回二进制中1的个数
def num_of_1(num):
    cnt = 0
    while num:
        mr = most_right(num)
        # num如果是负数，不能直接减
        num ^= mr
        cnt += 1
    return cnt


if __name__ == "__main__":
    arr = [1, 3, 1, 7]
    # print(binary_search_exist(arr, 6))
    # print(once(arr))
    # print(most_right(26))
    # print(two_once(arr))
    print(num_of_1(3))
