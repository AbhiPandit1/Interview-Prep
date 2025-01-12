# isko valid hone ke lie do conditoon he first the graph edges should all be connected so no of edges should be 
# equal to n-1 and next that it does not have a cycle 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)!=n-1:
            return False
        
        adj={i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit=[False]*n
        
        def dfs(node,parent):

            if visit[node]==True:
                return False
            visit[node]=True
            
            for nei in adj[node]:
                if not visit[nei]:
                    if dfs(nei,node):
                        return True
                elif parent!=nei:
                    return True
            
            return False
        
        for i in range(n):
            if not visit[i]:
                if dfs(i,-1):
                    return False
        return True
                

        