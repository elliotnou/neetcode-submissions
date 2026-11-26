class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # simplest solution
        # go through points, compute the euclidean distance to origin (O(n))
        # create a min-heap with the distances
        # add the top k in the minheap

        # there can be same distances so cannot do a distance-point mapping

        

        points = [[(points[i][0] ** 2 + points[i][1] ** 2) ** (1/2), i, [points[i][0], points[i][1]]] for i in range(len(points))]
        heapq.heapify(points)

        ret = []
        while k > 0:
            ret.append(list(heapq.heappop(points)[2]))
            k -=1
        
        return ret
