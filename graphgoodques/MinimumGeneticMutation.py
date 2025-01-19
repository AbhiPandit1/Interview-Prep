# simple step har mutation ko array me rkh ke usse send krdo ye thoda tricky he
# then uss mutation pe bas bfs chla do simple with visit set also ok and return the step with appropriate condition

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def geneMutation(gene):
            mutations=[]

            for i in range(len(gene)):
                for ch in "ACGT":
                    mutation = gene[:i] + ch + gene[i+1:]
                    mutations.append(mutation)
            return mutations
        
        def bfs():
            

            steps=0

            queue=[(startGene,steps)]

            visit=set()

            while queue:
                start,step=queue.pop(0)

                if start==endGene:
                    return step
                visit.add(start)
                
                
                for mutation in geneMutation(start):
                    if mutation in bank and mutation not in visit:
                        
                        queue.append((mutation,step+1))
            return -1
        
        return bfs()
                



        
                
