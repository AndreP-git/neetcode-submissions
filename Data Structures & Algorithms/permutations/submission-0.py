class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def generate_permutations(candidate: List[int]):
            if len(candidate) == len(nums):
                ans.append(list(candidate))
                return
            
            for i in range(len(nums)):
                if nums[i] in candidate:
                    continue
                candidate.append(nums[i])
                generate_permutations(candidate)
                candidate.pop()
            
        ans = []
        generate_permutations([])
        return ans