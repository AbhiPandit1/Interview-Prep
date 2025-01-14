# shortespath mtlb djikestra algorithm
# phle normla graph banao with the help of adj
# then use a minHeap to store starting position and final destination
# when run it through pop it check if it is in visit if it is continue else t= w1 and
# kepp on going through it neighbora nd keep on updating the time
# and adding on the visit
# then return the time if the len(visit)==n else we can t reach it 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj=defaultdict(list)

        for u,v,w in times:
            adj[u].append([v,w])

        minH=[(0,k)]
        visit=set()

        t=0

        while minH:
            w1,v1=heapq.heappop(minH)
            if v1 in visit:
                continue
            visit.add(v1)
            t=w1

            for vi,weight in adj[v1]:
                if vi not in visit:
                    heapq.heappush(minH,[w1+weight,vi])
        
        if len(visit)==n:
            return t
        return -1