# https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        p1 = l1
        p2 = l2
        result = None
        p = result
        while p1 is not None and p2 is not None:
            num = p1.val + p2.val + flag
            if num >= 10:
                flag = 1
                num = num % 10
            else:
                flag = 0
            
            if result is None:
                result = ListNode(num)
                p = result
            else:
                p.next = ListNode(num)
                p = p.next
            
            p1 = p1.next
            p2 = p2.next
        
        while p1 is not None:
            num = p1.val + flag
            if num >= 10:
                flag = 1
                num = num % 10
            else:
                flag = 0
            
            p.next = ListNode(num)
            p = p.next
            p1 = p1.next

        while p2 is not None:
            num = p2.val + flag
            if num >= 10:
                flag = 1
                num = num % 10
            else:
                flag = 0
            
            p.next = ListNode(num)
            p = p.next
            p2 = p2.next

        if flag == 1:
            p.next = ListNode(1)

        return result
        
