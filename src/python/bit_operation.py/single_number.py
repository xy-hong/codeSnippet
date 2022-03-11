# leetcode 136
# https://leetcode-cn.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        i = 1
        length = len(nums)
        while i < length:
            result ^= nums[i] 
            i += 1

        return result
