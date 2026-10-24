class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # def rob_house(i: int):
        #     if i >= len(nums):
        #         return 0
            
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = max(nums[i] + rob_house(i+2), rob_house(i+1))
        #     return cache[i]

        # cache = {}
        # return rob_house(0)

        # if len(nums) == 1: return nums[0]

        # cache = [0] * len(nums)
        # cache[0] = nums[0]
        # cache[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     cache[i] = max(nums[i] + cache[i-2], cache[i-1])
        
        # return cache[-1]

        if len(nums) == 1: return nums[0]
        
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = curr
            curr = max(nums[i] + prev, curr)
            prev = temp
        
        return curr
