class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, where the bucket's indices are how frequent the number occurs
        # the bucket length is nums, as a number can occur up to k times

        bucket = [[] for _ in range(len(nums)+1)] # set up k buckets
        res = []
        visited = defaultdict(int)
        for n in nums:
            visited[n] += 1
        
        for num, freq in visited.items():
            bucket[freq].append(num)

        m = len(nums) - 1
        while len(res) < k:
            res.extend(bucket[m])
            m -= 1
        
        return res

