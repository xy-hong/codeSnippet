# https://leetcode-cn.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        stack = []
        i = 0
        length = len(s)
        while i < length:
            c = s[i]
            if c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False        
            else:
                stack.append(c)

            i += 1
        
        if len(stack) > 0:
            return False
        
        return True