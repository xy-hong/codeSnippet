# https://leetcode-cn.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        table = [
            (1, 'I'),
            (4, 'IV'),
            (5, 'V'),
            (9, 'IX'),
            (10, 'X'),
            (40, 'XL'),
            (50, 'L'),
            (90, 'XC'),
            (100, 'C'),
            (400, 'CD'),
            (500, 'D'),
            (900, 'CM'),
            (1000, 'M'),       
        ]

        num = 0
        table = table[::-1]
        for val, symbol in table:
            while s.startswith(symbol):
                num += val
                s = s[len(symbol):]
        
        return num
