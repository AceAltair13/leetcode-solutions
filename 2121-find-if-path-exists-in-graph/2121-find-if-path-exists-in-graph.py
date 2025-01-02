class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        stack = []

        stack += adj_list[source]
        visited.add(source)

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            if node not in visited:
                visited.add(node)
                for x in adj_list[node]:
                    if x not in visited:
                        stack.append(x)
        
        return False