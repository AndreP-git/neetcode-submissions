class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def generate_subsets(candidate: List[int], idx: int):
            if len(candidate) == len(nums):
                ans.append(candidate[:])
                return
            
            ans.append(candidate[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                candidate.append(nums[i])
                generate_subsets(candidate, i+1)
                candidate.pop()
        
        nums.sort()
        ans = []
        generate_subsets([], 0)
        return ans