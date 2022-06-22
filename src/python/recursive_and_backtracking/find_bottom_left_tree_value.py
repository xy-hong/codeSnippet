# leetcode 513
# https://leetcode.cn/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return leftvalue(root, 0)[0]

    
def leftvalue(node, deep) -> (int, int):
        
    if node.left:
        leftTree = leftvalue(node.left, deep+1)
    else:
        leftTree = (node.val, deep)
    
    if node.right:
        rightTree =  leftvalue(node.right, deep+1)
    else:
        rightTree = (node.val, deep)
    
    if leftTree[1] >= rightTree[1]:
        return leftTree
    else:
        return rightTree
