# Bfs se krenge to kahn algorithm se 
# dfs se krenge to undirected cycle traversal and keep on appending in our stack
# atlast check if stack==numCourses

# Dfs
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj={i:[] for i in range(numCourses)}

        for n1,n2 in prerequisites:
            adj[n2].append(n1)
        
        parent=[False]*len(adj)
        visit=[False]*len(adj)
        stack=[]

        def dfs(node):

            if visit[node]:
                return False
            if parent[node]:
                return True
            visit[node]=True
            parent[node]=True
            
            for nei in adj[node]:
                if not visit[nei]:
                    if dfs(nei):
                        return True
                if parent[nei]:
                    return True
            parent[node]=False
            stack.append(node)
            return False
        
        for i in range(len(adj)):
            if not visit[i]:
                if dfs(i):
                    return []
                    
        return stack[::-1]
        