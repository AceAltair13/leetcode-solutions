"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def clone_with_dfs(node):
            if not node:
                return

            if node in hashmap:
                return hashmap[node]
            
            _node = Node(node.val)
            hashmap[node] = _node

            for x in node.neighbors:
                _node.neighbors.append(clone_with_dfs(x))
            
            return _node
        
        return clone_with_dfs(node)
