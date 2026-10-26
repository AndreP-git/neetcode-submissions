class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # def dp(idx1: int, idx2: int):
        #     if idx1 == len(text1) or idx2 == len(text2):
        #         return 0
            
        #     if (idx1, idx2) in cache:
        #         return cache[(idx1, idx2)]
            
        #     if text1[idx1] == text2[idx2]:
        #         cache[(idx1, idx2)] = dp(idx1 + 1, idx2 + 1) + 1
        #     else:
        #         cache[(idx1, idx2)] = max(dp(idx1 + 1, idx2), dp(idx1, idx2 + 1))

        #     return cache[(idx1, idx2)]
        
        # cache = {}
        # return dp(0, 0)

        # cache = [[0 for _ in range(len(text2) + 1)]
        #             for _ in range(len(text1) + 1)]

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             cache[i][j] = cache[i+1][j+1] + 1
        #         else:
        #             cache[i][j] = max(cache[i][j+1], cache[i+1][j])
        
        # return cache[0][0]

        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        cache = [0 for _ in range(len(text2) + 1)]

        for i in range(len(text1)-1, -1, -1):
            prev = 0
            for j in range(len(text2)-1, -1, -1):
                temp = cache[j]
                if text1[i] == text2[j]:
                    cache[j] = prev + 1
                else:
                    cache[j] = max(cache[j], cache[j+1])
                prev = temp
        return cache[0] 