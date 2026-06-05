class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def insert(self, node):
        secondRight = self.right.prev
        secondRight.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = secondRight
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])    
        self.insert(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
