# clone krne ke lie copy krna he or fir usme change krna he like copyCLone=me clone value naam ki node create kro
# then go through neighbors of node and then appenit inside copyClone[node].neighbors me through recursive function

#BFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        copyClone={}
        
        queue=[node]
        copyClone[node] = Node(node.val)

        while queue:
            root=queue.pop(0)
            

            for nei in root.neighbors:
                if nei not in copyClone:
                    copyClone[nei]=Node(nei.val)
                    queue.append(nei)
                copyClone[root].neighbors.append(copyClone[nei])
        return copyClone[node]