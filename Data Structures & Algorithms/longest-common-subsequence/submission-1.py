class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dp(idx1: int, idx2: int):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            
            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]
            
            if text1[idx1] == text2[idx2]:
                cache[(idx1, idx2)] = dp(idx1 + 1, idx2 + 1) + 1
            else:
                cache[(idx1, idx2)] = max(dp(idx1 + 1, idx2), dp(idx1, idx2 + 1))
                
            return cache[(idx1, idx2)]
        
        cache = {}
        return dp(0, 0)