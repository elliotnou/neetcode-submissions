class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we iterate over nums.
        # initialize a hashmap where key is DIFFERENCE, value is INDEX
        # for each element, we check if target - element is in the KEYs of the hashmap. if so, return an array with the value of that key, current index
        # if not, add the curr element as a key and the index as the value (unless it already exists)
        hm = defaultdict(list)
        for i, n in enumerate(nums):
            diff = target-n
            if diff in hm.keys():
                return [hm[diff][0], i]
            else:
                hm[n].append(str(i))