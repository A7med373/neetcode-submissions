class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict()
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        print(freq)
        freq = dict(sorted(freq.items(), key=lambda value: value[1], reverse=True))
        print(freq)
        return list(freq.keys())[:k]