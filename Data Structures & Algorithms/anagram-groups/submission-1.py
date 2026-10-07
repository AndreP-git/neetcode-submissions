class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = defaultdict(list)

        for s in strs:
            curr = [0] * 26
            
            for c in s:
                curr[ord(c) - 97] += 1
            

            counter[tuple(curr)].append(s)

            
        return list(counter.values())