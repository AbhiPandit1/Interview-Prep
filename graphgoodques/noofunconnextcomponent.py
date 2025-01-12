# isme jaise ki hume batana he how many no connected component are ther
# just check for no of components do dfs and check how many time dfs run and return count
# we can also do it using union find how many time we have to run union


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj={i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n2].append(n1)
            adj[n1].append(n2)
        
       
        visit=[False]*n
        def dfs(node):

            
            visit[node]=True
            

            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
            
        
        count=0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                count+=1
        return count
    
    
    class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        par=[i for i in range(n)]
        rank=[1]*n

        def find(n1):
            res=n1

            while res!=par[res]:
                par[res] = par[par[res]]  # Path compression
                res = par[res]
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)

            if p1==p2:
                return 0
            
            if rank[p2]>rank[p1]:
                par[p1]=par[p2]
                rank[p1]+=rank[p2]
            else:
                par[p2]=par[p1]
                rank[p2]+=rank[p1]
            return 1
        res=n

        for n1,n2 in edges:
            res-=union(n1,n2)
        return res
