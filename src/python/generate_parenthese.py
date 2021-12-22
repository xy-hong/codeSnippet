# https://leetcode-cn.com/problems/generate-parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur_str = ''
        result = []
        left = n
        right = n

        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                result.append(cur_str)
                return
            if left > right:
                return
            
            if left > 0:
                dfs(cur_str + '(', left -1, right)

            if right > 0:
                dfs(cur_str + ')', left, right -1)    
        
        dfs(cur_str, left, right)
        return result