class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = defaultdict(int)
        counts[s[l]] += 1
        result = 1
        
        while r < len(s) - 1:
            r += 1
            counts[s[r]] += 1

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result