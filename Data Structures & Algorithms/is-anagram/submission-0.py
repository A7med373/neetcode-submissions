# class Solution:
#       Time: (nlong + mlogm)
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         return False

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = 97
        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - a] += 1
            letters[ord(t[i]) - a] -= 1
        for i in range(len(letters)):
            if letters[i] != 0:
                return False
        return True
        