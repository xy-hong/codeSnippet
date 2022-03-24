# leetcode 661
# https://leetcode-cn.com/problems/image-smoother/
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        max_x = len(img)
        max_y = len(img[0])
        result = [[0]*max_y for _ in range(max_x) ]

        def getAvager(x, y) -> int:
            sum = img[x][y]
            count = 1
            if x - 1 >= 0 and y - 1 >= 0:
                count += 1
                sum += img[x-1][y-1]
            if x - 1 >= 0:
                count += 1
                sum += img[x-1][y]
            if x - 1 >= 0 and y + 1 < max_y:
                count += 1
                sum += img[x-1][y+1]

            if y - 1 >= 0:
                count += 1
                sum += img[x][y-1]
            if y + 1 < max_y:
                count += 1
                sum += img[x][y+1]
            
            if x + 1 < max_x and y - 1 >= 0:
                count += 1
                sum += img[x+1][y-1]
            if x + 1 < max_x:
                count += 1
                sum += img[x+1][y]
            if x + 1 < max_x and y + 1 < max_y:
                count += 1
                sum += img[x+1][y+1]
            
            return int(sum / count)

        for x in range(max_x):
            for y in range(max_y):
                result[x][y] = getAvager(x, y)

        return result
