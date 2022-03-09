# leetcode 46
# https://leetcode-cn.com/problems/permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)

        def backtrace(current: List[int], rest: List[int]):
            if len(current) == length:
                result.append(current)
            
            for x in range(len(rest)):
                backtrace(current+[rest[x]], rest[:x]+rest[x+1:])

        
        for i in range(length):
            backtrace([nums[i]], nums[:i]+nums[i+1:])

        return result