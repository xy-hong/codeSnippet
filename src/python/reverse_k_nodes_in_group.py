# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        # 只有一个节点，翻转与否不重要
        if head.next is None:
            return head

        stack = []
        p = head
        while len(stack) < k:
            if p is not None:
                stack.append(p)
                p = p.next
            else:
                break

        if len(stack) == k:
            head = stack[-1]
            while len(stack) > 0:
                if len(stack) == 1:
                    node = stack.pop()
                    node.next = self.reverseKGroup(p, k)
                    break
                node = stack.pop()
                node.next = stack[-1]
                
        elif len(stack) < k:
            return stack[0]
        
        return head