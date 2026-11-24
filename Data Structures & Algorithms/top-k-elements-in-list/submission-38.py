class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency of a number can be from 0 to len(nums)
        # create a bucket where index is frequency, val is a list of numbers that occur at that frequency

        ret = []
        numdict = defaultdict(int)
        for n in nums:
            numdict[n] += 1
        
        buckets = [[] for i in range(len(nums))]

        for key, value in numdict.items():
            buckets[value-1].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
