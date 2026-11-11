class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRULinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def evictLRU(self):
        lru = self.left.next
        self.remove(lru)
        return lru.key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.linkList = LRULinkedList()
        
    # remove from current position
    # append to LL
    # return val from lookup
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self.linkList.remove(node)
        self.linkList.add(node)
        return self.lookup[key].val
    
    # remove from current position if it exists
    # append to LL and add to lookup
    # if capcicty is exceeded, remove LRU (node on the left)
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.linkList.remove(node)
        newNode = ListNode(key, value)
        self.linkList.add(newNode)
        self.lookup[key] = newNode
        if len(self.lookup) > self.capacity:
            lru = self.linkList.evictLRU()
            del self.lookup[lru]

        
