# https://leetcode-cn.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrace(use_list: List[int], tmp: List[int]):
            if len(tmp) == len(nums):
                result.append(tmp)
                return
            
            for i in range(len(use_list)):
                backtrace(use_list[:i] + use_list[i+1:], tmp + [use_list[i]])
        
        backtrace(nums, [])
        return result

