# leetcode 278
# https://leetcode-cn.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        
        left = 1
        right = n

        while left < right:
            mid = int((left + right) / 2)
            if isBadVersion(mid) and isBadVersion(right):
                right = mid
            elif not isBadVersion(mid):
                if left + 1 == right:
                    left = right
                else:
                    left = mid

        return left