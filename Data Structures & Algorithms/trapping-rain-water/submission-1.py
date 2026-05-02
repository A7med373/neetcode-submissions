class Solution:
    def trap(self, height: List[int]) -> int:
        # result = min(lmax, rmax) - height[i]
        if not height:
            return 0
        n = len(height)
        area = 0
        # Brute Force
        """for i in range(n):
            lmax = rmax = 0
            for j in range(i):
                lmax = max(lmax, height[j])
            for j in range(i + 1, n):
                rmax = max(rmax, height[j])
            tmp = min(lmax, rmax) - height[i] 
            area += tmp if tmp >= 0 else 0
        return area"""
        # Prefix suffix
        prefix = [0] * n
        suffix = [0] * n 
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        
        suffix[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])
        for i in range(n):
            area += min(prefix[i], suffix[i]) - height[i]
        return area
        # Two Pointers