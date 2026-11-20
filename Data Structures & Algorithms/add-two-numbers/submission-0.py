# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        

        new_list = ListNode(-1)
        temp = new_list
        carry = 0
        while l1 and l2:

            num1 = l1.val
            l1 = l1.next
            num2 = l2.val
            l2 = l2.next
            digit = carry + num1 + num2

            carry = digit//10
            digit = digit%10
            temp.next = ListNode(digit)
            temp = temp.next
        
        while l1:
            num1 = l1.val
            l1 = l1.next
            digit = carry + num1
            carry = digit//10
            digit = digit%10
            temp.next = ListNode(digit)
            temp = temp.next
        while l2:
            num2 = l2.val
            l2 = l2.next
            digit = carry + num2
            carry = digit//10
            digit = digit%10
            temp.next = ListNode(digit)
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
            temp = temp.next
        
        return new_list.next
