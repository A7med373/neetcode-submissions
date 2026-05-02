class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash Map
        """freq = defaultdict()
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        freq = dict(sorted(freq.items(), key=lambda value: value[1], reverse=True))
        return list(freq.keys())[:k]"""
        # Bucker Sort
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
        