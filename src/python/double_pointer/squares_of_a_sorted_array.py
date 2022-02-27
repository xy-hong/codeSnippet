# leetcode 977
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/submissions/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 全部都是非负数
        if nums[0] >= 0:
            return [x**2 for x in nums]
        
        # 全部都是非正数
        if nums[-1] <= 0:
            return list(reversed([x**2 for x in nums]))
        
        non_negative = 0
        negative = 0
        nums_len = len(nums)

        for i in range(nums_len):
            if nums[i] < 0 and nums[i+1] >= 0:
                negative = i
                non_negative = i + 1
                break
        
        result = []
        while negative >= 0 and non_negative < nums_len:
            left = nums[negative] ** 2
            right = nums[non_negative] ** 2
            
            if left == right:
                result.append(left)
                result.append(right)
                negative -= 1
                non_negative += 1
            elif left < right:
                result.append(left)
                negative -= 1
            elif left > right:
                result.append(right)
                non_negative += 1
        
        while negative >= 0:
            result.append(nums[negative]**2)
            negative -= 1
        
        while non_negative < nums_len:
            result.append(nums[non_negative]**2)
            non_negative += 1
        
        return result

if __name__ == '__main__':
    print(Solution().sortedSquares([-1]))

            
