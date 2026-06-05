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
        curr = head
        while curr:
            copy = Node(curr.val, curr.next, curr.random)
            curr.next = copy
            curr = copy.next

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
