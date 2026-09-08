class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        weighted_adj = defaultdict(list)

        # Construct graph
        for i, e in enumerate(equations):
            x, y = e
            weighted_adj[x].append((y, values[i]))
            weighted_adj[y].append((x, 1 / values[i]))
        
        # DFS
        visited = set()
        def dfs(u, target, curr_product):

            if u == target:
                return curr_product
            
            for v, weight in weighted_adj[u]:
                if v in visited:
                    continue

                visited.add(v)
                result = dfs(v, target, curr_product * weight)
                visited.remove(v)
                if result != -1:
                    return result
                    
            return -1
        
        result = []
        for u, v in queries:
            if u not in weighted_adj or v not in weighted_adj:
                result.append(-1)
                continue
            result.append(dfs(u, v, 1))
        return result


