class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # one pass for a dictionary of the frequency of each number
        # sort
        # one pass for extracting the top k
        nums = sorted(nums)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i, c in count.items():
            freq[c].append(i)

        retarr = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                retarr.append(n)
                if len(retarr) == k:
                    return retarr




        


