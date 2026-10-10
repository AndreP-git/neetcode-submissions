class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # [1,2,2,3,3,3]
        # counter = {1: 1, 2: 2, 3: 3}

        from collections import Counter
        counter = Counter(nums)

        from heapq import heappush, heappop
        heap = []
        for key, val in counter.items():
            heappush(heap, (val, key))
            while len(heap) > k:
                heappop(heap)

        return [key for val, key in heap]