class Solution:

    def encode(self, strs: List[str]) -> str:
        #   4#str 7#str 12#str
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # 4#aaaa3#aaa5#aaaaaa
        i = 0
        res = []

        while i < len(s):
            
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])

            i = j + 1 + length 
        
        return res