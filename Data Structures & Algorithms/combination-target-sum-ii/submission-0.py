class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def generate_combinations(curr: set(), curr_sum: int, idx: int):
            if curr_sum == target:
                ans.append(curr[:])
                return
            
            if curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                generate_combinations(curr, curr_sum + candidates[i], i + 1)
                curr.pop()

        candidates.sort()
        ans = []
        generate_combinations([], 0, 0)
        return ans