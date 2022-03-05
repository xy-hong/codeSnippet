# leetcode 733
# https://leetcode-cn.com/problems/flood-fill/

# breadth first search 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        init = image[sr][sc]

        if init == newColor:
            return image
        
        max_row = len(image)
        max_col = len(image[0])

        q = []
        q.append({"row": sr, "col": sc})

        while len(q) > 0:
            item = q.pop(0)
            row = item['row']
            col = item['col']
            image[row][col] = newColor

            if row - 1 >= 0 and image[row-1][col] == init:
                q.append({"row": row - 1, "col": col})

            if row + 1 < max_row and image[row+1][col] == init:
                q.append({"row": row + 1, "col": col})
            
            if col - 1 >= 0 and image[row][col-1] == init:
                q.append({"row": row, "col": col - 1})
            
            if col + 1 < max_col and image[row][col+1] == init:
                q.append({"row": row, "col": col+1})
        
        return image