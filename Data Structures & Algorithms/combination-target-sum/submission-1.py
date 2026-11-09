class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def generate_combinations(candidate: List[int], curr_sum: int, idx: int):
            if curr_sum == target:
                ans.append(candidate[:])
                return
            
            if curr_sum > target:
                return
            
            for i in range(idx, len(nums)):
                candidate.append(nums[i])
                generate_combinations(candidate, curr_sum + nums[i], i)
                candidate.pop()
        
        ans = []
        generate_combinations([], 0, 0)
        return ans