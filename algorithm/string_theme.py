# 判断有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return
        if len(s) % 2 == 1:
            return False
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack


# 判断是否是回文字符串
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return
        new_s = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            else:
                left+=1
                right-=1
        return True


# 反转字符串
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        len_s = len(s)
        for i in range(len_s//2):
            tmp_right = s[len_s-i-1]
            tmp_left = s[i]
            s[i] = tmp_right
            s[len_s-i-1] = tmp_left

    # 计算两个字符串的乘积
    def multiply(self, num1, num2):
        #把num1,num2翻转方便计算
        num1 = num1[::-1]; num2 = num2[::-1]
        #每一位互相乘的结果用一维数组去储存
        arr = [0 for i in range(len(num1)+len(num2))]
        #填充这个一维数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
        ans = []
        #计算每一位的终极结果
        for i in range(len(arr)):
            #digit表示这一位的数字
            digit = arr[i] % 10
            #carry表示加给下一位的量
            carry = arr[i] / 10
            if i < len(arr)-1:
                #下一位加上
                arr[i+1] += carry
            #更新答案
            ans.insert(0, str(digit))
        #去除首位为0的情况
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        #连接成字符串
        return ''.join(ans)



