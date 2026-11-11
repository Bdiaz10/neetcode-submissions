# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev
        
        leftPrev = None
        resultHead = None
        left = head
        right = head
        count = 0
        while right:
            count += 1
            if count == k:
                tmpNext = right.next
                right.next = None
                newHead = reverse(left)
                if leftPrev:
                    leftPrev.next = newHead
                else:
                    resultHead = newHead


                leftPrev = left
                left.next = tmpNext
                left = left.next
                right = left
                count = 0
            else:
                right = right.next

        return resultHead

        
