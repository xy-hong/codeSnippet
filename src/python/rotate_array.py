# leetcode 189
# https://leetcode-cn.com/problems/rotate-array/submissions/
# 解法一：翻转整个数组，再从位置 k 切开，分别翻转两个子数组
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        reverse_nums(nums, 0, len(nums) -1)
        reverse_nums(nums, 0, k-1)
        reverse_nums(nums, k, len(nums) -1)


def reverse_nums(nums: List[int], start: int, end: int):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    

