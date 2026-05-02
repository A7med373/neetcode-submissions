class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        # Brute Force O(n^3)
        """result = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(i) for i in result]"""
        # Hash Map
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        res = []
        for i in range(n):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
            for j in range(i + 1, n):
                count[nums[j]] += 1
        return res
                
        # Two Pointers