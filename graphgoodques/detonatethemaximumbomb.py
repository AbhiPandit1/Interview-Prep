# achha question h graph banana aana chye isme condition yaad rkhni h
# (x1-x2)**2+(y1-y2)**2<=r**2 agr he to jo dusra wala hoga wo hmare graph he uske area me aayega
# issi se graph bana ke append krlo i k andar
# now from every bomb bfs maar do ki kon kon se part hum jaa paa rhe he
# and maximum wala return krdo 

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # (x**2+y**2)**2<=r**2 then the point is in range of the given

        adj=defaultdict(list)

        for i in range(len(bombs)):
            x1,y1,r1 =bombs[i]

            for j in range(len(bombs)):
                if i != j:
                    x2,y2,r2=bombs[j]

                    if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2:
                        adj[i].append(j)
        
        def bfs(i):

            queue=[i]
            visit=set()
            visit.add(i)

            while queue:
                n1=queue.pop(0)

                for j in adj[n1]:
                    if j not in visit:
                        visit.add(j)
                        queue.append(j)
            
            return len(visit)
        
        max_bomb=0
        for i in range(len(bombs)):
            max_bomb=max(max_bomb,bfs(i))
        return max_bomb
        