# leetcode 617
# https://leetcode-cn.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None and root2 is None:
            return None
        
        mergeNode = None
        if root1 is None:
            mergeNode = TreeNode(root2.val)
            mergeNode.left = self.mergeTrees(None, root2.left)
            mergeNode.right = self.mergeTrees(None, root2.right)
        
        elif root2 is None:
            mergeNode = TreeNode(root1.val)
            mergeNode.left = self.mergeTrees(root1.left, None)
            mergeNode.right = self.mergeTrees(root1.right, None)
        
        else:
            mergeNode = TreeNode(root1.val + root2.val)
            mergeNode.left = self.mergeTrees(root1.left, root2.left)
            mergeNode.right = self.mergeTrees(root1.right, root2.right)
        
        return mergeNode
        