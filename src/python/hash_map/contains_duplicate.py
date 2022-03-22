# leetcode 217
# https://leetcode-cn.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for n in nums:
            if numMap.get(n):
                return True
            numMap[n] = True
        
        return False