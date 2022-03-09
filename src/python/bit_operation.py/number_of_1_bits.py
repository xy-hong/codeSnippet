# leetcode 191
# https://leetcode-cn.com/problems/number-of-1-bits/submissions/
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        
        count = 0
        while n != 0:
            if n == n | 1:
                count += 1
            n = n >> 1
        
        return count