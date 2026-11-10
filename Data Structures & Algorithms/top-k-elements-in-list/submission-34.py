class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency is in a range from 0 to len(nums)
        buckets = [[] for i in range(len(nums)+1)]

        ret = []
        freq = defaultdict(int)
        # we first map the numbers to frequencies
        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            buckets[val].append(key)
        
        for l in range(len(buckets)-1, -1, -1):
            for n in buckets[l]:
                ret.append(n)
                if len(ret) == k:
                    return ret
            

