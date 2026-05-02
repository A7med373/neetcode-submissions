class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for index, number in enumerate(nums):
            indexes[number] = index
        for index, number in enumerate(nums):
            difference = target - number
            if difference in indexes and indexes[difference] != index:
                return [index, indexes[difference]]