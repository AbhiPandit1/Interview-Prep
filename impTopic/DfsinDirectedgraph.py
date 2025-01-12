# simple he directed me alg se parent lena eh then solve it


def dfsDirected(node,adj):
    parent=[]*len(adj)
    visit=[]*len(adj)
    
    visit[node]=True
    parent[node]=True
    
    for nei in adj[node]:
        if not visit[nei]:
            if dfsDirected(nei,adj):
                return True
        if  parent[nei]:
            return True
    parent[node]=False
    return False
            
        