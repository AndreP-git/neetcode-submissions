class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_house(i: int):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + rob_house(i+2), rob_house(i+1))
            return cache[i]

        cache = {}
        return rob_house(0)