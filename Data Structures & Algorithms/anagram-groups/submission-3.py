class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        letters = [[0 for _ in range(26)] for _ in range(len(strs))]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                letters[i][ord(strs[i][j]) - ord('a')] += 1
            key = tuple(letters[i])
            if key not in group:
                group[key] = []
            group[key].append(strs[i])
        return list(group.values())
            