class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # must start a two pointer, l and r
        # we know that the height of the pool must be bound by the minimum height between left and right
        # we only MOVE when the wall is larger than the minimum of the heights of the left and right
        l, r = 0, len(heights) - 1

        volume = 0
        while l < r:
            volume = max(volume, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
                r -= 1


        
            
            
        
        return volume
        