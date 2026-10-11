class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_len, curr_len = 0, 0

        for num in nums:
            curr_len = curr_len + 1 if num else 0
            max_len = max(max_len, curr_len)
        
        return max_len