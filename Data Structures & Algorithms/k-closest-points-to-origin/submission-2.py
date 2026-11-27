class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # the heap needs to order based on DISTANCE (minheap) but also store the POINTS.
        # let the heap store [dist, x, y]
        for i, p in enumerate(points):
            x, y = p
            dist = x**2 + y**2
            points[i] = [dist, x, y]
        
        heapq.heapify(points) # minheap based on distance!

        ret = []
        while k > 0:
            dist, x, y = heapq.heappop(points)
            ret.append([x, y])
            k -=1
        
        return ret

