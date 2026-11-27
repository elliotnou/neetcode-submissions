class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # two heaviest stones at each step. dont need order but need some way to retrieve the two heaviest stones in the least amount of tie possible
        #use a max-heap

        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, x - y)
            
        return abs(stones[0]) if stones else 0

        