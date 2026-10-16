# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def searchMin(root): 
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        def remove(root, key):
            if not root:
                return None
            
            if key > root.val: 
                root.right = remove(root.right, key)
            elif key < root.val:
                root.left = remove(root.left, key)
            else: 
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = searchMin(root.right)
                    root.val = minNode.val
                    root.right = remove(root.right, minNode.val)
            return root
        
        return remove(root, key)