# https://leetcode-cn.com/problems/min-cost-climbing-stairs/
class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2:
            return 0
        
        min_cost = [0] * (n+1)
        for i in range(2, n+1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])

        return min_cost[-1]

    # 递归
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n < 2:
            return 0
        
        n_2 = self.minCostClimbingStairs(cost[:-2]) + cost[n-2]
        n_1 = self.minCostClimbingStairs(cost[:-1]) + cost[n-1]

        return min(n_2, n_1)
        
    