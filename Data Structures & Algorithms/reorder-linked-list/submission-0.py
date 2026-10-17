# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def pop(curr):
            if not curr: return None
            while curr and curr.next and curr.next.next:
                curr = curr.next
            
            node = curr.next
            curr.next = None
            return node
        
        while head and head.next:
            n = pop(head)
            tmp = head.next
            head.next = n
            head.next.next = tmp
            head = tmp
        


        
        # on current node:
        #   pop() from end
        #   tmp = curr.next
        #   curr.next = popped()
        #   curr.next.next = tmp
        #   curr = tmp