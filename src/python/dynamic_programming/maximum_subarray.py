# leetcode 53
# https://leetcode-cn.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        f = [0] * length
        f[0] = nums[0]
        i = 1
        while i < length:
            if f[i-1] > 0:
                f[i] = f[i-1] + nums[i]
            else:
                f[i] = nums[i]

            i += 1
        
        return max(f)