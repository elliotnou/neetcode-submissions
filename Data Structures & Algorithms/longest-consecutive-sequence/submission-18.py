class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input: unsorted list of ints (duplicates allowed)
        # Output: length of longest run of values that go up by 1. O(n)

        # Examples: [10, 6, 5, 8, 9, 2, 1] -> 3 
        # Edge cases:
            # [] -> 0
            # [1] -> 1
            # [3, 3, 3, 3] -> 1
            # [4, 3, 2, 1] -> 4
            # [-1, 0, 1] -> 3
            # [1, 3, 5, 7] -> 1

        # Brute force method: to try and search for a consecutive sequence with every element being the "start" -> O(n^2)

        # Only search for a consecutive sequence starting with nums[i] if nums[i] - 1 is not in the array. membership check of a hashset is O(1)

        numset = set(nums)
        ret = 0
        for n in numset:
            maxlen = 1
            if n-1 not in numset:
                # this n can be a start, so we check longest
                while n+maxlen in numset:
                    maxlen += 1
                ret = max(maxlen, ret)
        return ret








        
                


