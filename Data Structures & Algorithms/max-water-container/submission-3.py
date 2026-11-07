class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: an array of integer heights
        # Output: an int, the max volume

        # Edge cases:
            # [1, 1] -> 1
            # [1, 1, 1, 6, 7, 2, 1, 1] -> 42
            # [0, 100] -> 0
        
        # approach: use a two pointer approach, capturing the max at each time
        # the volume is capped by the height of the minimum wall, so move the pointer of the minimum wall in at each step, and log the vol

        l = 0
        r = len(heights) - 1
        vol = 0
        while l < r:
            curvol = min(heights[l], heights[r])*(r-l)
            vol = max(curvol, vol)
            if heights[l]<=heights[r]:
                l += 1
            else:
                r -= 1
            
        return vol
