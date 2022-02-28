# leetcode 283
# https://leetcode-cn.com/problems/move-zeroes/

# 解法一：O(n^2)
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return
        
        left = 0
        while left < length - 1:
            if nums[left] == 0:
                right = left + 1
                while right < length:
                    if nums[right] != 0:
                        nums[left], nums[right] = nums[right], nums[left]
                        break
                    right += 1
            
            left += 1

# 解法二：O(n^1)
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        fast = 0
        slow = 0
        for i in range(length):
            if nums[i] == 0:
                slow = i
                fast = i + 1
                break
        
        while fast < length:
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
                    