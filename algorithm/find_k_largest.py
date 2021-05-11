# 第一种
def find_k_largest1(in_list, k):
    in_list.sort()
    return in_list[-k]


# 第二种
def find_k_largest2(in_list, k):
    kmax = [float('-inf')] * k
    for i in range(len(in_list)):
        j = 0
        while j < k:
            if in_list[i] > kmax[j]:
                kmax[j+1:] = kmax[j:k-1]
                kmax[j] = in_list[i]
                break
            else:
                j += 1
    return kmax[k - 1]


if __name__ == "__main__":
    input_list = [6, 4, 2, 1, 8, 5]
    print(find_k_largest1(input_list, 3))
    print(find_k_largest2(input_list, 3))