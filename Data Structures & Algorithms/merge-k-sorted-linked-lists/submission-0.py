# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # naive solution : 
        # 1. Push all the nodes to a min_heap
        # 2. keep popping
        
        if not lists : return None

        heap = []
        cnt = 1
        for head in lists:
            while head:
                heapq.heappush(heap, (head.val, cnt, head))
                head = head.next
                cnt+=1
        print(len(heap))

        if heap :
            _, _, curr = heapq.heappop(heap)
            head = curr
        else : 
            return None
        while heap:
            _, _, nxt = heapq.heappop(heap)
            curr.next = nxt
            curr = nxt
        return head
        
        