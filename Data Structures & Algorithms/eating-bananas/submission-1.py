class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force
        k = 1
        while True:
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            if total_time <= h:
                return k
            k += 1
        return k
        # Binary Search