class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = [[0 for _ in range(26)] for _ in range(len(strs))]
        group_map = {}
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                groups[i][ord(strs[i][j]) - ord('a')] += 1
            key = tuple(groups[i])
            if key not in group_map:
                group_map[key] = []
            group_map[key].append(strs[i])
        return list(group_map.values())