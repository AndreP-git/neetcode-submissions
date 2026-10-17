# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # def inorder(root):
        #     if not root:
        #         return
            
        #     nonlocal ans, count

        #     inorder(root.left)
        #     count += 1
        #     if count == k:
        #         ans = root.val
        #     inorder(root.right)

        # ans = -1
        # count = 0
        # inorder(root)
        # return ans

        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val

            curr = curr.right
        

