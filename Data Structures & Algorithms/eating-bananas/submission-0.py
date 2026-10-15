class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(speed: int) -> bool:
            from math import ceil
            return sum(ceil(pile / speed) for pile in piles) <= h

        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left