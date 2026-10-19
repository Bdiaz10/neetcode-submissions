"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copies = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copies[curr] = copy
            curr = curr.next
    
        dummy = Node(0)
        curr = dummy
        while head:
            copies[head].next = copies[head.next]
            copies[head].random = copies[head.random]

            dummy.next = copies[head]
            dummy = dummy.next
            head = head.next

        return curr.next
        