# https://leetcode-cn.com/problems/even-odd-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even_list = [root]
        odd_list = []

        flag = 'even'
        while len(odd_list) > 0 or len(even_list) > 0:
            if flag == 'even':
                pre_val = 0
                while len(even_list) > 0:
                    node = even_list.pop(0)
                    if (node.val % 2 == 0) or node.val <= pre_val:
                        return False
                    else:
                        if node.left is not None:
                            odd_list.append(node.left)
                        if node.right is not None:
                            odd_list.append(node.right)
                    pre_val = node.val
                flag = 'odd'
            else:
                pre_val = 999999999
                while len(odd_list) > 0:
                    node = odd_list.pop(0)
                    if (node.val % 2 == 1) or node.val >= pre_val:
                        return False
                    else:
                        if node.left is not None:
                            even_list.append(node.left)
                        if node.right is not None:
                            even_list.append(node.right)
                    pre_val = node.val
                flag = 'even'
        
        return True