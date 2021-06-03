class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        head, curr, n1, n2 = None, None, l1, l2
        # Keep two pointers (n1, n2) on each list (l1, l2)
        while n1 and n2:
            if n1.val < n2.val:
                if curr: curr.next = n1
                else: head = n1
                curr = n1
                n1 = n1.next
            else:
                if curr: curr.next = n2
                else: head = n2
                curr = n2
                n2 = n2.next
        # Remaining list elements
        if n1:
            curr.next = n1
        else:
            curr.next = n2
        return head

