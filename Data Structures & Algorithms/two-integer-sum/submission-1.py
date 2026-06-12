class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies = {}
        for index, num in enumerate(nums):
            indecies[num] = index
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indecies:
                return [i, indecies[difference]]