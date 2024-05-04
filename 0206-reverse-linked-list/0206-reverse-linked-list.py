# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head
        
        """
        :type head: ListNode
        :rtype: ListNode
        """
        