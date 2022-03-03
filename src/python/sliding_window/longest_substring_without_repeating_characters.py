# leetcode 3
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        map = {}
        max_length = 0

        while right < len(s):
            c = s[right]
            if c in map:
                left = max(map[c] + 1, left)
            max_length = max(max_length, right - left + 1)
            map[c] = right
            right += 1
        
        return max_length
