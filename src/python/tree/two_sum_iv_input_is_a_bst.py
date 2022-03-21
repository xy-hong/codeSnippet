# leetcode 653
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        
        q = []
        def mid_travel(r):
            if r is None:
                return
            
            mid_travel(r.left)
            q.append(r.val)
            mid_travel(r.right)
        
        mid_travel(root)
        l = 0
        r = len(q) - 1
        while l < r:
            if q[l] + q[r] == k:
                return True
            elif q[l] + q[r] > k:
                r -= 1
            elif q[l] + q[r] < k:
                l += 1
            
        return False

            
