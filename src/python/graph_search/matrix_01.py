# leetcode 542
# https://leetcode-cn.com/problems/01-matrix
from typing import List
# 思路：以 0 为起点扩散，计算每个 1 的距离
# 先遍历整个二维数组，把 0 加入队列，把 1 赋值为 -1 表示未访问过。
# 队列中的依次出队，每次访问出队元素的相邻四个位置，如果是 -1 ，则赋值为 出队元素值 +1
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_row = len(mat)
        max_col = len(mat[0])

        q = []
        for i in range(max_row):
            for j in range(max_col):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1
        
        while len(q) > 0:
            x, y = q.pop(0)
            
            # 四个方向的 x y 变化
            dxs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in dxs:
                new_x = x + dx
                new_y = y + dy
                if (0 <= new_x < max_row) and (0 <= new_y < max_col) and mat[new_x][new_y] == -1:
                    mat[new_x][new_y] = mat[x][y] + 1
                    q.append((new_x, new_y))
        
        return mat

if __name__ == '__main__':
    Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])