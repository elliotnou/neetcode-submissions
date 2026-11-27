class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we want an O(n log k), that is, the heap should only carry k elements at once always
        # let us build a heap with the first k elements of nums, and then put the LATTER half into the heap popping and pushing

        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        
        return heap[0]