"""
给出一组数字，找出每个元素右边的第一个大于它的数，如果没有标记为 -1
例子 
输入 [15, 2, 8, 13]
输出 [-1, 8, 13, -1]
"""
from typing import List


s = [15, 2, 8, 13]

# 遍历，时间复杂度 O(n^2)
def nextBig(s: List) -> List:
    result = []
    length = len(s)
    i = 0
    while i < length:
        j = i
        a = s[i]
        while j < length:
            b = s[j]
            if b > a:
                result.append(b)
                break
            j += 1

        if j == length:
            result.append(-1)

        i += 1 
    
    return result

# 借助 stack
def nextBig2(s: List) -> List:
    length = len(s)
    i = 1
    stack = [0]
    result = [0] * length
    while i < length:
        value = s[i]
        if value > s[stack[-1]]:
            while len(stack) > 0:
                stackIndex = stack[-1]
                stackValue = s[stackIndex]
                if value > stackValue:
                    result[stackIndex] = value
                    stack.pop()
                else:
                    stack.append(i)
                    break
        else:
            stack.append(i)
        i += 1
    
    while len(stack) > 0:
        result[stack.pop()] = -1

    return result

assert nextBig(s) == [-1, 8, 13, -1]
assert nextBig2(s) == [-1, 8, 13, -1]