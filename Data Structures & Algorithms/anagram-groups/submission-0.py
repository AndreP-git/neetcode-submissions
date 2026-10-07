class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = {}

        for s in strs:
            curr = [0] * 26
            
            for c in s:
                curr[ord(c) - 97] += 1
            
            if tuple(curr) in counter:
                counter[tuple(curr)].append(s)
            else:
                counter[tuple(curr)] = [s]
            
        return list(counter.values())