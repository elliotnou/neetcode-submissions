class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first pass, a dict where the key is the number and the val is the freq
        # then, a second pass through the dict, creating a bucket where index is the FREQ and the elements are LISTS of the numbers that occur that many times.

        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key, val in count.items(): # key is the number, value is the frequency
            bucket[val].append(key)
        

        res = []
        for m in range(len(bucket)-1, 0, -1):
            for elem in bucket[m]:
                res.append(elem)
                if len(res) == k:
                    return res
        
            



                
                







