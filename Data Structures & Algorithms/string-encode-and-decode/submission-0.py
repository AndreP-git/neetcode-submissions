class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#str1 7#str2
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0
    
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            curr_len = int(s[i:j])
            curr_str = s[j+1 : j+1+curr_len]
            res.append(curr_str)
            i = j + 1 + curr_len
        
        return res