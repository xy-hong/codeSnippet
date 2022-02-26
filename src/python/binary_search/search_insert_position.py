# leetcode 35
# https://leetcode-cn.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        
        if target == nums[-1]:
            return len(nums) - 1
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int((left + right) / 2)

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        
        # 此时 left == right
        return left + 1 if target > nums[left] else left