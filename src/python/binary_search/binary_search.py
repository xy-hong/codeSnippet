# leetcode 704
# https://leetcode-cn.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = len(nums) - 1
        

        while left <= right:
            mid = int((left + right) / 2)
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        
        return -1