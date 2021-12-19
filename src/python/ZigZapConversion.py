# https://leetcode-cn.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        if len(s) <= numRows:
            return s
        
        rows = []
        for x in range(numRows):
            rows.append([])

        isDown = False
        row_index = 0
        for i in range(len(s)):
            rows[row_index].append(s[i])
            if row_index == 0 or row_index == numRows - 1:
                isDown = not isDown
            
            if isDown:
                row_index += 1
            else:
                row_index -= 1
        
        result = ''
        for row in rows:
            result += ''.join(row)
        
        return result