class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # [1,2,2,3,3,3] k=2
        # dict = {1: 1, 2: 2, 3: 3}
        # [3:3, 2:2, 1:1] --> [3, 2]

        counter = Counter(nums)
        
        items = list(counter.items())

        items.sort(key=lambda item: item[1], reverse=True)

        return [k for k, v in items][:k]
        