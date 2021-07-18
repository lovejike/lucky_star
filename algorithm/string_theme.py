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



