# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half with slow/fast pointers
        # reverse the second half
        # merge both ll, taking one from each
        if not head.next:
            return None
        def printLL(node):
            while node:
                print(node.val)
                node = node.next
            print('\n')

        def reverseLL(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev

        leftHead = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rightHead = slow

        curr = head
        while curr:
            if curr.next == slow:
                curr.next = None
                break
            curr = curr.next


        rightHead = reverseLL(rightHead)
        printLL(leftHead)
        printLL(rightHead)
        
        dummy = ListNode()
        while leftHead and rightHead:
            dummy.next = leftHead
            leftHead = leftHead.next
            dummy = dummy.next

            dummy.next = rightHead
            rightHead = rightHead.next
            dummy = dummy.next
        


        
       