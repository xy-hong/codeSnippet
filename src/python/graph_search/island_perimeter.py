# leetcode 463
# https://leetcode-cn.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        
        def wps(x: int, y: int) -> int:
            perimeter = 0
            grid[x][y] = 2
            q = [(x,y)]
            while len(q) > 0:
                i, j = q.pop()
                p = 4
                if i + 1 < max_row and grid[i+1][j] > 0:
                    if grid[i+1][j] == 1:
                        grid[i+1][j] = 2
                        q.append((i+1, j))
                    p -= 1
                if i - 1 >= 0 and grid[i-1][j] > 0:
                    if grid[i-1][j] == 1:
                        grid[i-1][j] = 2
                        q.append((i-1, j))
                    p -= 1
                if j + 1 < max_col and grid[i][j+1] > 0:
                    if grid[i][j+1] == 1:
                        grid[i][j+1] = 2
                        q.append((i,j+1))
                    p -= 1
                if j - 1 >= 0 and grid[i][j-1] > 0 :
                    if grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        q.append((i, j-1))
                    p -= 1

                perimeter += p         

            return perimeter

        for x in range(max_row):
            for y in range(max_col):
                if grid[x][y] == 1:
                    return wps(x, y) 