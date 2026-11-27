class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we always start with the task that has the highest count
        # after doing that task, push to a queue that stores the (COUNT, TIME when it can be done again)

        freq = Counter(tasks) 
        maxHeap = [-n for n in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        t = 0
        while maxHeap or q:
            t += 1
            if not maxHeap:
                t = q[0][1]  # jump to the time 
            else:
                task = abs(heapq.heappop(maxHeap))
                if task > 1:
                    q.append([task-1, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, -q.popleft()[0])
                
            
       
        return t

