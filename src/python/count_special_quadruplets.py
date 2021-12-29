# https://leetcode-cn.com/problems/count-special-quadruplets/
# 暴力破解
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                for c in range(b+1, len(nums)):
                    for d in range(c+1, len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            result += 1
        
        return result

# 使用字典存储 d
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        length = len(nums)
        counts = [0] * 1000
        for c in range(length-2, 1, -1):
            d = c + 1
            counts[nums[d]] += 1
            for b in range(c-1, 0, -1):
                for a in range(b-1, -1, -1):
                    if counts[ nums[a] + nums[b] +nums[c] ] > 0:
                        result += counts[nums[a] + nums[b] +nums[c]]
        
        return result
