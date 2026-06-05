class Node:
    def __init__(self, val: int, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.tail.prev = self.head
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        lastNode = self.tail.prev
        newNode = Node(value, lastNode, self.tail)
        lastNode.next = newNode
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        firstNode = self.head.next
        newNode = Node(value, self.head, firstNode)
        firstNode.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastNode = self.tail.prev
        prevLastNode = lastNode.prev
        ret = lastNode.val

        prevLastNode.next = self.tail
        self.tail.prev = prevLastNode
        
        return ret

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        firstNode = self.head.next
        secondNode = firstNode.next
        ret = firstNode.val
        secondNode.prev = self.head
        self.head.next = secondNode
        return ret
