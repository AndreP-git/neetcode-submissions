class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        from heapq import heapify, heappush, heappop

        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            x, y = -heappop(stones), -heappop(stones)
            if abs(x - y) > 0:
                heappush(stones, -abs(x - y))
        
        return -stones[-1] if stones else 0
