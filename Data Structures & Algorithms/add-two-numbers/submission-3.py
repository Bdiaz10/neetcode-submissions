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
            l1Val = 0
            l2Val = 0
            if l1:
                l1Val = l1.val
            if l2:
                l2Val = l2.val
                
            total = l1Val + l2Val + carry
            carry = 0
            if total > 9:
                carry = 1
                total = total % 10
            dummy.next = ListNode(total)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # while l1:
        #     total = l1.val + 0 + carry
        #     carry = 0
        #     if total > 9:
        #         carry = 1
        #         total = total % 10
        #     dummy.next = ListNode(total)
        #     dummy = dummy.next
        #     l1 = l1.next
        
        # while l2:
        #     total = 0 + l2.val + carry
        #     carry = 0
        #     if total > 9:
        #         carry = 1
        #         total = total % 10
        #     dummy.next = ListNode(total)
        #     dummy = dummy.next
        #     l2 = l2.next

        if carry:
            dummy.next = ListNode(1)

        return pointer.next
