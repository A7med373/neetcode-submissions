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
        for i in range(n):
            l, r = i + 1, n - 1
            temp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif numbers[mid] > temp:
                    r = mid - 1
                else:
                    l = mid + 1
        return []
        # Hash Map
        # Two pointers
