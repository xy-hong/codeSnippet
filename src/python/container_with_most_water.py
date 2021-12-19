# https://leetcode-cn.com/problems/container-with-most-water/
# 双指针，从数组左右设置 left, right。 每次移动短的那根，求面积。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(min_height * (right - left), max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area