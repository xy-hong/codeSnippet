# leetcode 231
# https://leetcode-cn.com/problems/power-of-two/
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
            
        count = 0
        while n != 0:
            if n | 1 == n:
                count += 1
            n = n >> 1
        
        if count == 1:
            return True
        
        return False
#
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
