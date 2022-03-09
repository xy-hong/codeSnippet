# leetcode 77
# https://leetcode-cn.com/problems/combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        init = [x for x in range(1,n+1)]
        result = []

        def callback(current: List[int], rest: List[int], k: int):
            if len(current) == k:
                if current not in result:
                    result.append(current)
                return
            
            # 从 rest 选一个，然后 rest 只变成被选元素后面的元素（保证组合元素都是递增的，就不会出现重复）
            for x in range(len(rest)):
                callback(current+[rest[x]], rest[x+1:], k)
            
        initLength = len(init)
        for i in range(initLength):
            callback([init[i]], init[i+1:], k)

        return result