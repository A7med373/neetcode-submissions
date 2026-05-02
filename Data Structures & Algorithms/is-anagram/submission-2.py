class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorting
        return sorted(s) == sorted(t)
        # Arrays