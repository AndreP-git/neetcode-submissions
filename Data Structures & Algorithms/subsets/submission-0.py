class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def generate_subsets(idx: int, candidate: List[int]):

            if len(candidate) > len(nums):
                return
            
            ans.append(candidate[:])

            for i in range(idx, len(nums)):
                candidate.append(nums[i])
                generate_subsets(i+1, candidate)
                candidate.pop()
            
        ans = []
        generate_subsets(0, [])
        return ans

