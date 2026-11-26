class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # simplest solution
        # go through points, compute the euclidean distance to origin (O(n))
        # create a min-heap with the distances
        # add the top k in the minheap

        # there can be same distances so cannot do a distance-point mapping

        
        heap = []
        for x, y in points:
            heap.append([(x**2 + y**2) ** (1/2), x, y])
        heapq.heapify(heap)

        ret = []
        while k > 0:
            point = heapq.heappop(heap)
            ret.append([point[1], point[2]])
            k -= 1
        
        return ret
