# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def printLL(node):
            while node:
                print(node.val)
                node = node.next
            print('\n')

        def split(node) -> list:
            prev = None
            slow = node
            fast = node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            rightHead = slow
            if prev:
                prev.next = None
            return [node, rightHead]
        
        def reverseLL(node) -> ListNode:
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev
        
        def mergeLL(left, right):
            dummy = ListNode()
            while left and right:
                dummy.next = left
                left = left.next
                dummy = dummy.next

                dummy.next = right
                right = right.next
                dummy = dummy.next

            if right:
                dummy.next = right

        if not head.next:
            return
        left, right = split(head)
        printLL(left)
        printLL(right)

        right = reverseLL(right)
        printLL(right)

        mergeLL(left, right)


        