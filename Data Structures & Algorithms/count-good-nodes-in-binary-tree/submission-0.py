# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: Optional[TreeNode], curr_max: int):
            if not node:
                return
            
            nonlocal good
            if node.val >= curr_max:
                good += 1
            curr_max = max(curr_max, node.val)
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
        
        good = 0
        dfs(root, -101)
        return good
