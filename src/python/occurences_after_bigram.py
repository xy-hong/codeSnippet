# https://leetcode-cn.com/problems/occurrences-after-bigram/
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result = []
        length = len(words)
        i = 0
        while i < length:
            if words[i] == first:
                if i + 1 < length and words[i+1] == second:
                    if i + 2 < length:
                        result.append(words[i+2])
            i += 1
        
        return result