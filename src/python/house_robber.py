# https://leetcode-cn.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        # return max(self.rob(nums[:-2]) + nums[n-1], self.rob(nums[:-1]))
        max_rob = [0] * n
        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0], nums[1])
        for i in range(2, n):
            max_rob[i] = max(max_rob[i-2]+nums[i], max_rob[i-1])
        
        return max_rob[-1]