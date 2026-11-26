

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we maintain a maxHeap that has the next thing to process 9always go from highest frequency)
        # we maintain a queue that pushes to the maxHeap when the time is sufficiently cooled down

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
    
        t = 0
        while maxHeap or q:
            t += 1
            # suppose nothing in the heap -- everything is in queue to cool down. then, time jump
            if not maxHeap:
                t = q[0][1]
            else:
                cnt = -heapq.heappop(maxHeap) - 1
                if cnt:
                    q.append([cnt, t + n])
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, -q.popleft()[0])
            
        return t

