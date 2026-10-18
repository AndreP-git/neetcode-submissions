class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def generate_combinations(candidate: List[int], idx: int, curr_sum: int):
            if curr_sum > target:
                return
            
            if curr_sum == target:
                ans.append(candidate[:])
                return 
            
            for i in range(idx, len(nums)):
                candidate.append(nums[i])
                generate_combinations(candidate, i, curr_sum + nums[i])
                candidate.pop()
            
        ans = []
        generate_combinations([], 0, 0)
        return ans
