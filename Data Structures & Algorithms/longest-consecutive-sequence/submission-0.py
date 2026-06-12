class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 1
        for num in nums:
            temp = 1
            if num - 1 in nums:
                continue
            while num + 1 in nums:
                temp += 1
                num += 1
            length = max(length, temp)
        return length