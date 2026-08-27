# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list1 or list2
        
        new_list = ListNode(-1)
        temp = new_list

        while list1 and list2:
            new_val = None
            if list1.val>list2.val:
                new_val = list2.val
                list2 = list2.next
            else:
                new_val = list1.val
                list1 = list1.next
            
            temp.next = ListNode(new_val, None)
            temp = temp.next
        
        temp.next = list1 or list2

        return new_list.next
