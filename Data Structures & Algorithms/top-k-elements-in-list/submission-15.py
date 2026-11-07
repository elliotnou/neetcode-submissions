class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first, we sort the array
        # then, we must do a bucketsort where the index is FREQUENCY and the value is   a LIST of the numbers in nums that occur that frequent
        # then, store the most frequent numbers until length of the res is k.



        sortednums = sorted(nums)
        arr = {i : [] for i in range(len(nums) + 1)} # create a dict

        i = 0
        while i < len(sortednums):
            count = 1
            while i != len(sortednums)-1 and sortednums[i] == sortednums[i+1]:
                count += 1
                i += 1
            arr[count].append(sortednums[i])
            i += 1
            
        res = []
        for i in range(len(arr)-1, -1, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
            
                

        


                
                







