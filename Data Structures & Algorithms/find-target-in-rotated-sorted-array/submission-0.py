class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            # 3 4 5 6 1 2  -1:4
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m
            else:
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    l = m + 1
                elif nums[m] < target:
                    r = m
        return -1
                