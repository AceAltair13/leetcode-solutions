# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _k = k
        ans = 0

        def inorder(node):
            nonlocal _k, ans
            if not node:
                return
                
            inorder(node.left)
            if _k == 1:
                ans = node.val
            _k -= 1
            
            if _k > 0:
                inorder(node.right)

        inorder(root)

        return ans