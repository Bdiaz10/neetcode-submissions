# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # to remove a node, we need the node and its previous node
        #   * handle when the node is the head
        fast = head
        for i in range(1, n):
            fast = fast.next
        prev = None
        targetNode = head
        while fast and fast.next:
            prev = targetNode
            targetNode = targetNode.next
            fast = fast.next
        
        # handle remove head:
        if not prev:
            return targetNode.next
        
        prev.next = targetNode.next
        return head
        
