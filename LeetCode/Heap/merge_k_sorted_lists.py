from typing import *
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        curr = ListNode(None)
        result = curr

        # start with the first nodes of each list
        for i in range(len(lists)):
            node = lists[i]
            if node:
                # add dummy variable i, so that no comparison btw node happens
                heapq.heappush(heap, (node.val, i, node))

        while len(heap) > 0:
            item = heapq.heappop(heap)
            curr.next = item[2]
            curr = item[2]

            next_node = item[2].next
            # keep pushing the next node of the popped node, until there is no node in the list
            if next_node:
                heapq.heappush(heap, (next_node.val, item[1], next_node))
        return result.next