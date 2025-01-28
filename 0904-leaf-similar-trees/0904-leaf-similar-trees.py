# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq_1 = []
        seq_2 = []

        def traverse(node, seq):
            if node:
                if not node.left and not node.right:
                    seq.append(node.val)
                else:
                    traverse(node.left, seq)
                    traverse(node.right, seq)
        
        traverse(root1, seq_1)
        traverse(root2, seq_2)

        return seq_1 == seq_2