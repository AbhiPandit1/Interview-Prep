class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        adj={i:[] for i in range(len(graph))}

        degree={i:0 for i in range(len(graph))}

        for i in range(len(graph)):
            for v in graph[i]:
                adj[v].append(i)
                degree[i] += 1
        
        queue=[]
        safe_node=set()
        
        for node in degree:
            if degree[node]==0:
                queue.append(node)
        
        while queue:
            root=queue.pop()
            safe_node.add(root)

            for nei in adj[root]:
                degree[nei]-=1

                if degree[nei]==0:
                    queue.append(nei)
        return sorted(safe_node)

     
     
     
     
     