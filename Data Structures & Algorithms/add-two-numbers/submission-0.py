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
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = 0
            if total > 9:
                carry = 1
                total = total % 10
            dummy.next = ListNode(total)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + 0 + carry
            carry = 0
            if total > 9:
                carry = 1
                total = total % 10
            dummy.next = ListNode(total)
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            total = 0 + l2.val + carry
            carry = 0
            if total > 9:
                carry = 1
                total = total % 10
            dummy.next = ListNode(total)
            dummy = dummy.next
            l2 = l2.next
        if carry:
            dummy.next = ListNode(1)

        return pointer.next
