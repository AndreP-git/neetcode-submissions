class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = {}
        for c in s1:
            c1[c] = c1.get(c, 0) + 1
        
        c2 = {}
        left = 0

        for right in range(len(s2)):
            c2[s2[right]] = c2.get(s2[right], 0) + 1

            if right >= len(s1):
                
                c2[s2[left]] = c2[s2[left]] - 1
                if c2[s2[left]] == 0:
                    del c2[s2[left]]
                left += 1

            if c1 == c2:
                return True
        
        return False
        