class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        idx = 0
        for num in range(len(count)):
            for _ in range(count[num]):
                nums[idx] = num
                idx += 1
        