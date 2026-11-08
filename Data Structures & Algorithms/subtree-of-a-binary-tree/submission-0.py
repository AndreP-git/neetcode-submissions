# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def find_candidates(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            if node.val == subRoot.val:
                candidates.append(node)

            find_candidates(node.left)
            find_candidates(node.right)

        def compare_trees(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            
            left = compare_trees(p.left, q.left)
            right = compare_trees(p.right, q.right)
            return p.val == q.val and left and right

        candidates = []
        find_candidates(root)

        for c in candidates:
            if compare_trees(c, subRoot) == True:
                return True
        return False


