# phle unidrected he mtlb dono trf se juda hua he 0--1 se connect hoga to 1 bb 0 se connect hoga
# isme ek visit set lena he 
# every time we will visit the node will return True and the we will go through the neighbour of each node
# and check if neighbor is not visited then we will run recursive and check for the cycle
# and if visited and node and nei is not the parent of nei then we will return True


adj = [[], [], [], []]
visit = [False] * len(adj)

def cycle(node, parent):
    visit[node] = True
    
    for nei in adj[node]:
        if not visit[nei]:
            if cycle(nei, node):  # Recursive DFS call
                return True
        elif nei != parent:  # Check for a back edge
            return True
    
    return False  # No cycle found in this path

# Main driver code
for i in range(len(adj)):
    if not visit[i]:
        if cycle(i, -1):  # Start DFS from unvisited nodes
            print(True)  # Cycle detected
            break
else:
    print(False)  # No cycle detected
