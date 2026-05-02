class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # Brute Force
        """
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        """
        # Binary Search
        """
        for i in range(n):
            diff = target - numbers[i]
            l, r = i + 1, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] > diff:
                    r = mid - 1
                else:
                    l = mid + 1
        return []
        """
        # Hash Map
        """hashmap = defaultdict(int)
        for i in range(n):
            diff = target - numbers[i]
            if hashmap[diff]:
                return [hashmap[diff], i + 1]
            hashmap[numbers[i]] = i + 1
        return []"""
        # Two pointers
        l, r = 0, n - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]
