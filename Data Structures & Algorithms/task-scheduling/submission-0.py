class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks[i] is a character from "A" to "Z"
        # tasks can be completed in any order
        # identical tasks must be separated by at least n CPU cycles

        # a max-heap of remaining counts, which decides which task runs next
        # a queue, which holds tasks when they cool down

        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        maxheap = [-x for x in freq.values()]
        heapq.heapify(maxheap)
        # we have [3, 2] for A A A B B
        print(maxheap)

        time = 0
        q = deque()

        while True:
            time += 1
            if maxheap:
                nexttask = -heapq.heappop(maxheap)
                if nexttask > 1: 
                    q.append([nexttask - 1, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, -q.popleft()[0])
            if len(q) == 0 and len(maxheap) == 0:
                return time







