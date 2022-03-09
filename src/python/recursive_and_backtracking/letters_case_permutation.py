# leetcode 784
# https://leetcode-cn.com/problems/letter-case-permutation
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        length = len(s)

        def trackback(current, k):
            if k == length:
                result.append("".join(current))
                return
            
            if not isLetter(s[k]):
                trackback(current + [s[k]], k + 1)
            else:
                trackback(current + [s[k]], k + 1)
                trackback(current + [turnCase(s[k])], k + 1)

            
        
        trackback([], 0)
        return result


def turnCase(s: str) -> str:
    no = ord(s[0])
    if ord('A') <= no <= ord('Z'):
        return s.lower()
    elif ord('a') <= no <= ord('z'): 
        return s.upper()

def isLetter(s: str) -> bool:
    no = ord(s[0])
    if ord('A') <= no <= ord('Z') or ord('a') <= no <= ord('z'):
        return True
    return False