# isme dfs use krenge har edge ko through dfs cycle wale meathod se cycle dhoondhenge if kisi bb edge 
# s e cycle milgya to hum use return krdenge 
# isse hum union find se bhi solve krskte the uski time complexity isse better rhegi
# kuki union find me cycle form ni hota if cycle hoga to wo hume retun krdena h
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}

        def dfs(node, parent):
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False

        for n1, n2 in edges:
            visit = [False] * (n + 1)  # Reset visit array for each edge
            adj[n1].append(n2)
            adj[n2].append(n1)

            if dfs(n1, -1):  # Check if adding this edge creates a cycle
                return [n1, n2]

        return []
