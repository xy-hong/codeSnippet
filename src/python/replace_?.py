# https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters
class Solution:
    def modifyString(self, s: str) -> str:
        length = len(s)
        if length == 1 and s[0] != '?':
            return s
        elif length == 1 and s[0] == '?':
            return 'a'

        cs = list(s)

        i = 0
        chars = ['a', 'b', 'c']
        while i < length:
            if s[i] == '?':
                j = 0
                while True:
                    cs[i] = chars[j]
                    if i == 0:
                        if cs[i] != cs[i+1]:
                            break
                    elif i == length -1:
                        if cs[i] != cs[i-1]:
                            break
                    else:
                        if cs[i] != cs[i+1] and cs[i] != cs[i-1]:
                            break
                    j = (j + 1) % 3
            i += 1   

        return "".join(cs)