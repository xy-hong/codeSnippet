# leetcode 567
# https://leetcode-cn.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False

        map1 = [0] * 26
        map2 = [0] * 26
        
        i = 0
        while i < len1:
            map1[get_ord(s1[i])] += 1
            map2[get_ord(s2[i])] += 1
            i += 1
        
        if map1 == map2:
            return True
        
        left = 0
        right = len1 - 1
        while right < len2:
            if map1 == map2:
                return True

            map2[get_ord(s2[left])] -= 1
            left += 1
            right += 1
            if right >= len2:
                break
            map2[get_ord(s2[right])] += 1
        return False

def get_ord(s) -> int:
    return ord(s) - ord('a')