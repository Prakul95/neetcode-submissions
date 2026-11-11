# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # last node ListNode(-1), ListNode(1), 2, 3
        # check for len(ls)-n difference
        # skip that node 

        dummy = ListNode(-1,head)

        if not head:
            return None
        
        slow = dummy
        fast = dummy
        temp = slow
        n+=1
        while n and fast:
            fast = fast.next
            n-=1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        if slow and slow.next:
            slow.next = slow.next.next
        
        return dummy.next


