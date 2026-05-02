class Solution:
    def trap(self, height: List[int]) -> int:
        # result = min(lmax, rmax) - height[i]
        if not height:
            return 0
        n = len(height)
        area = 0
        # Brute Force
        for i in range(n):
            lmax = rmax = 0
            for j in range(i):
                lmax = max(lmax, height[j])
            for j in range(i + 1, n):
                rmax = max(rmax, height[j])
            tmp = min(lmax, rmax) - height[i] 
            area += tmp if tmp >= 0 else 0
        return area
        # Prefix suffix
        # Two Pointers