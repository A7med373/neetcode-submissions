class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            for j in range(1, i):
                if nums[i] == nums[i-j]:
                    return True
        return False