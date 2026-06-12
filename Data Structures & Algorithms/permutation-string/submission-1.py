class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Using maps
        l = 0
        for r in range(len(s2)):
            tmp = defaultdict(int)
            for letter in s1:
                tmp[letter] += 1
            if s2[r] not in tmp:
                l = r
            other = r
            while other < len(s2) and s2[other] in tmp:
                tmp[s2[other]] -= 1
                other += 1
            if max(tmp.values()) == 0 and min(tmp.values()) == 0:
                return True
        return False
