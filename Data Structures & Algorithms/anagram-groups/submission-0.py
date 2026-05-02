class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        map = {}
        big_guy = [[0] * 26 for _ in range(length)]
        for i in range(length):
            for j in range(len(strs[i])):
                big_guy[i][ord(strs[i][j]) - ord('a')] += 1
            key = tuple(big_guy[i])
            if key not in map:
                map[key] = []
            map[key].append(strs[i])
        return list(map.values())