# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode()
        curr = head

        while heap:
            _, i, node = heapq.heappop(heap)
            lists[i] = lists[i].next
            curr.next = node
            curr = curr.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        return head.next