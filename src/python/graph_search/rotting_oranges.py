# leetcode 994
# https://leetcode-cn.com/problems/rotting-oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        q = []
        count = 0

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == 2:
                    q.append((i, j))
                    count += 1
                elif grid[i][j] == 1:
                    count += 1
                else:
                    continue
                    
        # 如果没有橘子，则没有新鲜橘子的时间为 0
        if count == 0:
            return 0
        
        minus = 0
        while len(q) > 0:
            x, y = q.pop(0)
            count -= 1
            minus = grid[x][y]

            dxs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in dxs:
                new_x = x + dx
                new_y = y + dy
                if (0 <= new_x < max_row) and (0 <= new_y < max_col) and grid[new_x][new_y] == 1:
                    q.append((new_x, new_y))
                    grid[new_x][new_y] = grid[x][y] +1
        
        if count > 0:
            return -1
        
        return minus - 2