# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,mv):
            if not node:
                return 0
            if node.val>=mv:
                res=1
            else:
                res=0
            mv=max(node.val,mv)
            res+=dfs(node.left,mv)
            res+=dfs(node.right,mv)
            return res
        return dfs(root,root.val)
        

        