class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indecies = {}
        for index, num in enumerate(nums):
            indecies[num] = index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indecies and i != indecies[diff]:
                return [i, indecies[diff]]
            