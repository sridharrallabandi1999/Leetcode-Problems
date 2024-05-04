# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head 
        for i in range(n):
            fast = fast.next
        if fast == None:
            return head.next           
        while(fast.next!=None):
            fast= fast.next
            slow = slow.next           
        deletnode=slow.next    
        slow.next = slow.next.next
        deletnode = None
        return head 
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        