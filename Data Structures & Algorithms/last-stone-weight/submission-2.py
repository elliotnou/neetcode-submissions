class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxheap

        heap = [-x for x in stones]
        heapq.heapify(heap) # O(n)

        while len(heap) > 1: # O(n)
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y > x:
                heapq.heappush(heap, x-y) #O(log n)

        heapq.heappush(heap, 0)
        return abs(heap[0])
        

