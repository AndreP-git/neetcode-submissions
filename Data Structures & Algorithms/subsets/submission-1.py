class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def generate_subsets(candidate: List[int], idx: int):
            if len(candidate) == len(nums):
                ans.append(candidate[:])
                return
            
            ans.append(candidate[:])
            for i in range(idx, len(nums)):
                candidate.append(nums[i])
                generate_subsets(candidate, i + 1)
                candidate.pop()
        
        ans = []
        generate_subsets([], 0)
        return ans

