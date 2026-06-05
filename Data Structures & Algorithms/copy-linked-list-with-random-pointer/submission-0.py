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
        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            node.next = copy
            node = copy.next
        
        copy = head.next
        while copy:
            if copy.next:
                copy.next = copy.next.next
            if copy.random:
                copy.random = copy.random.next
            copy = copy.next
        copy = head.next
        head.next = None
        return copy
