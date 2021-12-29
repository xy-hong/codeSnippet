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