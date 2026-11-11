class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node: ListNode):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node: ListNode):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def evict(self) -> int:
        lru = self.left.next
        self.remove(lru)
        return lru.key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.linkedlist = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self.linkedlist.remove(node)
        self.linkedlist.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.linkedlist.remove(node)
        newNode = ListNode(key, value)
        self.linkedlist.add(newNode)
        self.lookup[key] = newNode
        if len(self.lookup) > self.capacity:
            lru = self.linkedlist.evict()
            del self.lookup[lru]
        

        
