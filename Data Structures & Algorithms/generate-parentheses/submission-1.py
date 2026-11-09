class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(candidate: List[str], n_open: int, n_close: int):
            if len(candidate) == 2*n :
                ans.append("".join(candidate))
                return
            
            if n_open > 0:
                candidate.append("(")
                generate(candidate, n_open-1, n_close)
                candidate.pop()
            
            if n_close > n_open:
                candidate.append(")")
                generate(candidate, n_open, n_close-1)
                candidate.pop()
        
        ans = []
        generate([], n, n)
        return ans