# isme kuch ni krna bas count ka pata krna he uss hissab se array form krna he
# check if A[i] in seenb then update count and keep on appending in set
# similarly B[i] in seeA then update count and keep on appending in set

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        seeA=set()
        seeB=set()
        count=0
        res=[0]*len(A)

        for i in range(len(A)):

            if A[i] in seeB:
                count+=1
            seeA.add(A[i])

            if B[i] in seeA:
                count+=1
            seeB.add(B[i])

            res[i]=count
        return res
