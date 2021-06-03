from typing import *
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Runner based solution
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        rev = None
        # Reverse the links of the first half of the list
        while fast and fast.next:
            fast = fast.next.next
            orig_slow_next = slow.next
            rev, rev.next = slow, rev
            slow = orig_slow_next
        # Size is odd -> 'fast' is at the end of the list, 'slow' is at the exact middle
        if fast:
            slow = slow.next
        # At this point,
        # from the middle of the list, 'slow' is pointing towards the end of the list
        # from the middle of the list, 'rev' is pointing towards the start of the list
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True

    # Simple deque based solution
    # def isPalindrome(self, head: ListNode) -> bool:
    #     dq = collections.deque()
    #     curr_node = head
    #     while curr_node is not None:
    #         dq.append(curr_node.val)
    #         curr_node = curr_node.next
    #     while len(dq) >= 2:
    #         if dq.popleft() != dq.pop():
    #             return False
    #     return True


n5 = ListNode(1)
n4 = ListNode(2, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
s = Solution()
print(s.isPalindrome(n1))
