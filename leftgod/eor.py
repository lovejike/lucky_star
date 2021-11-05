# 1.异或运算，可用于计算只出现一次的数据
# 特性：N^0=N,N^N=0
def appear_only_once(arr):
    eor = 0
    for i in arr:
        eor = eor ^ i
    return eor

list = [0,1,1,2,2,3,3]
print(appear_only_once(list))