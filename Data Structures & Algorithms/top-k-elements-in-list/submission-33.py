class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the bucket can be len(nums)+1 (including the 0 freq)
        # we create a dict where key is the num and val is its freq
        # then we iterate on that dict and put it into buckets
        # then iterate on the buckets to get the top k freq
        ret = []
        bucket = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for key, value in freq.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
                