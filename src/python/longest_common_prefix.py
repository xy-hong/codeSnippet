# https://leetcode-cn.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        len_list = [len(x) for x in strs]
        min_len = min(len_list)
        i = 0
        result = ''
        while i < min_len:
            example = strs[0][i]
            for s in strs:
                if s[i] == example:
                    continue
                else:
                    return result
                
            result += example
            i += 1
        
        return result