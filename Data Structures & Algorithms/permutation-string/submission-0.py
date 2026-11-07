class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        s2_count = {}
        left = 0
        for right in range(len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            print(s2_count)
            if right >= len(s1):
                s2_count[s2[left]] = s2_count[s2[left]] - 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left += 1
            if s1_count == s2_count:
                return True
        
        return False
        