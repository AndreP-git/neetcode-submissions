# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # targetSum = 8, curr_sum = 1, res_left = True, res_right = True   --> True
        #    1
        #  2  3
        # 4 5  6

        # curr_sum + root.val --> explore left
        # leaf? --> check: curr_sum == targetSum --> return True else False
        # curr_sum - root.val --> backtrack

        def dfs(root: Optional[TreeNode], curr_sum: int):
            if not root:
                return False

            curr_sum += root.val
            if not root.left and not root.right:
                res = curr_sum == targetSum
                curr_sum -= root.val
                return res

            res_left = dfs(root.left, curr_sum)
            res_right = dfs(root.right, curr_sum)
            curr_sum -= root.val
            return res_left or res_right

        return dfs(root, 0)