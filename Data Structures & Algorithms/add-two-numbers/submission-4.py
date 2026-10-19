# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 327
        #  67
        # add using carry
        # for uneven sized lists, default to 0 for node val
        dummy = ListNode()
        pointer = dummy
        carry = 0
        while l1 or l2:
            l1Val = 0 if not l1 else l1.val
            l2Val = 0 if not l2 else l2.val
        
            total = l1Val + l2Val + carry
            carry = 0
            if total > 9:
                carry = 1
                total = total % 10
            dummy.next = ListNode(total)
            dummy = dummy.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

        if carry:
            dummy.next = ListNode(1)

        return pointer.next
