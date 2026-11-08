# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return True, float("inf"), float("-inf")
            
            left, left_min, left_max = dfs(node.left)
            right, right_min, right_max = dfs(node.right)

            return node.val > left_max and node.val < right_min and left and right, min(node.val, left_min), max(node.val, right_max)
        
        return dfs(root)[0]