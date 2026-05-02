class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        count = [[0 for _ in range(26)] for _ in range(len(strs))]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                count[i][ord(strs[i][j]) - ord('a')] += 1
            key = tuple(count[i])
            if key not in group:
                group[key] = []
            group[key].append(strs[i])
        return list(group.values())