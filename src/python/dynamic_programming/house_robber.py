# leetcode 198
# https://leetcode-cn.com/problems/house-robber
# f(n) = max(f(n-2)+nums[n], f(n-1))

# 超出时间限制
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0

#         if len(nums) == 1:
#             return nums[0]
        
#         return max(self.rob(nums[:-2]) + nums[-1], self.rob(nums[:-1]))

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        fn = [0] * len(nums)
        fn[0] = nums[0]
        fn[1] = max(nums[0], nums[1])

        i = 2
        while i < n:
            fn[i] = max(fn[i-2] + nums[i], fn[i-1])
            i += 1

        return fn[-1] 