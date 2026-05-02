class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, l, r = 0, 0, 0
        unique = set()
        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                result = max(result, r - l + 1)
                r += 1
            else:
                unique.remove(s[l])
                l += 1

        return result
