# leetcode 695
# https://leetcode-cn.com/problems/max-area-of-island/

# bfs, 先二重循环遍历每一个元素，当遇见岛屿时，以岛屿为起点进行 bfs
# 注意，在将岛屿添加入队时，就应该把岛屿变成 0，而不是出队时再变0，避免后面重复添加。
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        
        def bfs(x: int, y: int) -> int:
            count = 0
            q = []
            grid[x][y] = 0
            q.append((x, y))

            while len(q) > 0:
                row, col = q.pop(0)
                count += 1

                if row - 1 >= 0 and grid[row-1][col] == 1:
                    q.append((row-1, col))
                    grid[row-1][col] = 0
                if row + 1 < max_row and grid[row+1][col] == 1:
                    q.append((row+1, col))
                    grid[row+1][col] = 0
                if col - 1 >= 0 and grid[row][col-1] == 1:
                    q.append((row, col-1))
                    grid[row][col-1] = 0
                if col + 1 < max_col and grid[row][col+1] == 1:
                    q.append((row, col+1))
                    grid[row][col+1] = 0
                
            return count

        max_area = 0
        for x in range(max_row):
            for y in range(max_col):
                if grid[x][y] == 1:
                    max_area = max(bfs(x, y), max_area)

        return max_area