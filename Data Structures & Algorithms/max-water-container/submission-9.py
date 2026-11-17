class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # at any given point, the area is CAPPEd by the smaller wall.
        # use a 2 pointer traversal moving the one that is smaller
        # maintain max

        maxarea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[r], heights[l])
            maxarea = max(area, maxarea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxarea
