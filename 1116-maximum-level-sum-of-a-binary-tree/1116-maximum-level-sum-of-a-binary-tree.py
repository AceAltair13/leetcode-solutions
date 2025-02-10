# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(root)

        level_order = [[] for _ in range(height)]

        def traverse(node, level):
            if node:
                level_order[level].append(node.val)
                traverse(node.left, level + 1)
                traverse(node.right, level + 1)
        
        
        traverse(root, 0)

        sum_arr = []
        
        for level in level_order:
            sum_arr.append(sum(level))
        
        return sum_arr.index(max(sum_arr)) + 1
        