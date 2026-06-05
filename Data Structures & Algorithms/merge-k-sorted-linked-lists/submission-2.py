# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        res = ListNode(0)
        cur = res
        minHeap = []
        for lis in lists:
            if lis != None:
                heapq.heappush(minHeap, lis)
        while minHeap:
            node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, node.next)
        return res.next