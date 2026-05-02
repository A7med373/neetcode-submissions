class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxl = 0
        for num in nums:
            if num - 1 in nums:
                continue
            templ = 1
            while num + 1 in nums:
                templ += 1
                num += 1
            maxl = max(maxl, templ)
        return maxl
