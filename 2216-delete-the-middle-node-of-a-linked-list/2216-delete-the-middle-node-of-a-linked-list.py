# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        prev, slow, fast = head, head, head
        skip_first = True

        while fast and fast.next:
            if skip_first:
                skip_first = False
            else:
                prev = prev.next
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next

        return head