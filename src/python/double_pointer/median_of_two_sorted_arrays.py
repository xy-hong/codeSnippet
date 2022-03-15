# leetcode 4
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 == 0 and length2 == 0:
            return 0
                
        i = 0
        j = 0
        while True:
            if i == length1:
                sign = 1
                break
            
            if j == length2:
                sign = 2
                break

            n1 = nums1[i]
            n2 = nums2[j]
            if n1 < n2:
                result.append(n1)
                i += 1
            else:
                result.append(n2)
                j += 1
        
        if sign == 1:
            result += nums2[j:]
        
        if sign == 2:
            result += nums1[i:]
        
        resultLen = len(result)
        if resultLen % 2 == 0:
            index = int(resultLen/2)
            index2 = int(resultLen/2)-1
            return (result[index] + result[index2])/2
        else:
            index = int(resultLen / 2)
            return result[index]