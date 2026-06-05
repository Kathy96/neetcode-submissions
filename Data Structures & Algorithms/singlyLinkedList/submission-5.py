class Node:

    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1
            
    def insertHead(self, val: int) -> None:
        newNode = Node(val, self.head.next)
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
            

    def getValues(self) -> List[int]:
        cur = self.head.next
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
