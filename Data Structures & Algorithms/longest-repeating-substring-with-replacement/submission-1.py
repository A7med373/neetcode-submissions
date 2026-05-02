class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        # length = r - l + 1
        # X Y Y X
        count = defaultdict(int)
        result = 0
        while r < len(s):
            count[s[r]] += 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
            r += 1

        return result