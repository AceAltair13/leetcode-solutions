# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1

        def dfs(node, cur_sum):
            if not node:
                return 0
            
            cur_sum += node.val
            count = hashmap[cur_sum - targetSum]

            hashmap[cur_sum] += 1
            count += dfs(node.left, cur_sum) + dfs(node.right, cur_sum)
            hashmap[cur_sum] -= 1

            return count
        
        return dfs(root, 0)