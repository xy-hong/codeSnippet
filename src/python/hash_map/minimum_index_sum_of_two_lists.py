class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {}
        for x in range(len(list1)):
            map1[list1[x]] = x

        length = len(list2)
        minSum = 99999
        result = []
        i = 0
        while i < length:
            name = list2[i]
            index = map1.get(name)
            if index is not None:
                newValue = index + i
                if newValue < minSum:
                    minSum = newValue
                    result = [name]
                elif newValue == minSum:
                    result.append(name)

            i += 1
        
        return result