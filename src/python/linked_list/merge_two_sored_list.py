# https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 双指针
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        result = ListNode(-1)
        p = result
        move = list1
        stand = list2
        while move is not None:
            if move.val > stand.val:
                move, stand = stand, move
            
            p.next = ListNode(move.val)
            p = p.next
            move = move.next

        while stand is not None:
            p.next = ListNode(stand.val)
            p = p.next
            stand = stand.next
        
        return result.next       

# 递归
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        next1 = list1.next
        next2 = list2.next
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(next1, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, next2)
            return list2             



