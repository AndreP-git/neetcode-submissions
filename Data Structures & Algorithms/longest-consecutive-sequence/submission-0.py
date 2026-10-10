class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        max_len = 0
        for num in nums:
            curr_len = 1
            curr_val = num
            
            if curr_val - 1 not in nums:
                while curr_val + 1 in nums:
                    curr_len += 1
                    curr_val += 1
                max_len = max(max_len, curr_len)
            
        return max_len