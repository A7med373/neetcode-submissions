class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            # 3 5 1  -1:1
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
                elif nums[m] < target:
                    l = m + 1
                elif nums[m] > target and target < nums[r]:
                    l = m + 1
                elif nums[m] > target and target > nums[r]:
                    r = m
        return l if nums[l] == target else -1
                