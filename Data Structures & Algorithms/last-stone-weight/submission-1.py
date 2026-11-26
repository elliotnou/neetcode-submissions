class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxheap

        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if not x == y:
                heapq.heappush(heap, -abs(y - x))
        
        if len(heap) == 0:
            return 0
        else:
            return -heap[-1]

