class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]] = 1
            else:
                mapp[nums[i]] += 1
        mapp = dict(sorted(mapp.items(), key=lambda item: item[1], reverse=True))
        return list(mapp.keys())[:k]

