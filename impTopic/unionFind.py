
def __init__(self):
    self.par=[i for i in range(n)]
    self.rank=[1]*n


def find(self ,n1):
    res=n1
    
    while res!=self.par[res]:
        self.par[res]=self.find(res)
    
    return res

def union(self,n1,n2):
    p1,p2=self.find(n1),self.find(n2)
    
    if self.rank[p1]<self.rank[p2]:
        self.par[p1]=self.par[p2]
        self.rank[p1]+=self.rank[p2]
    else:
        self.par[p2]=self.par[p1]
        self.rank[p2]+=self.rank[p1]
    return 
        