class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        curr_sum = 0
        prefix = {0:1}

        for num in nums:
            curr_sum += num
            ans += prefix.get(curr_sum - k, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        
        return ans