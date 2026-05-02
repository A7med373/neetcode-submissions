class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorted 
        return sorted(s) == sorted(t)
        # Arrays
        if len(s) != len(t):
            return False
        letters = [0 for _ in range(26)]
        for i in range(s):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1
        for letter in letters:
            if letter != 0:
                return False
        return True