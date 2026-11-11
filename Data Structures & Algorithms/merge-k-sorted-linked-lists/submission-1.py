# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # list of linked lists
        # list can be empty
        # linked list can be empy
        
        # use a min heap to store current processing nodes
        # pop from minheap, add to LL, push node.next to minheap
        minheap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minheap, (head.val, i, head))
        
        dummy = ListNode()
        curr = dummy
        i = len(minheap)-1
        while minheap:
            val, _, node = heapq.heappop(minheap)
            curr.next = node
            curr = curr.next

            if curr.next:
                nxt = curr.next
                i += 1
                heapq.heappush(minheap, (nxt.val, i, nxt))

        return dummy.next
