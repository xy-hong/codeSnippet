# https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

                



