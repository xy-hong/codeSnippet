class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        key_boards = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        s = [[''], [''], [''], ['']]

        for i in range(len(digits)):
            s[int(i)] = key_boards[digits[i]]
        
        result = []
        for j in s[0]:
            for k in s[1]:
                for m in s[2]:
                    for n in s[3]:
                        result.append(j+k+m+n)
        
        return result
        