# https://leetcode-cn.com/problems/day-of-the-year/
class Solution:
    def dayOfYear(self, date: str) -> int:
        date_list = date.split('-')
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            month_list[1] = 29
        
        i = 0
        result = 0
        while i < month - 1:
            result += month_list[i]
            i += 1
        
        result += day

        return result
