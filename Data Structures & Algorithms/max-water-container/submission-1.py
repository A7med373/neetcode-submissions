class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        # Brute Force
        for i in range(n):
            for j in range(i + 1, n):
                area = max(area, (abs(i - j)) * min(heights[i], heights[j]))
        return area
        # Two Pointers
        """if not heights:
            return area
        l, r = 0, n - 1
        while l < r:
            area = max(area, (r - l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area"""