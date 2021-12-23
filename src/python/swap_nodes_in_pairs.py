# https://leetcode-cn.com/problems/swap-nodes-in-pairs
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        if head.next is None:
            return head
            
        s = head.next
        head.next = self.swapPairs(s.next)
        s.next = head
        return s
            