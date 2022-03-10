# leetcode 120
# https://leetcode-cn.com/problems/triangle
# f(x,y) = nums[x][y] + min(f(x+1, y), f(x+1,y+1))
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        
        f = [[] for i in range(n)]
        row = n - 1
        while row >= 0:
            for i in range(len(triangle[row])):
                if row == n - 1:
                    f[row].append(triangle[row][i])
                else:
                    f[row].append(min(f[row+1][i], f[row+1][i+1]) + triangle[row][i])
            row -= 1
        
        return f[0][0]
