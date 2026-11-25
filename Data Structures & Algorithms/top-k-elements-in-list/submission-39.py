class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the frequency of k can be from 0 to len(nums)

        # we use bucketsort, where the index is the FREQENCY and the value is a list of values that occur that many times

        freq = defaultdict(int)
        ret = []
        buckets = [[] for i in range(len(nums)+1)]

        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            buckets[val].append(key)
        
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret


            

