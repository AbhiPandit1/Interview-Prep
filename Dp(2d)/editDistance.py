# kuch ni krna simple template use krna he string ki equal he dono ko aage bdhao
# but if delete krna he to ek ko aage bdhao and ek ko waise hi rkho inser krna he to ek ko aage bdhao and ek 
# ko waise hi rkho but if replace krna he to dono aage bdh jyenge

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def helper(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i]==word2[j]:
                dp[(i,j)] =  helper(i+1,j+1)
            
            else:
                dp[(i,j)] = 1+min(helper(i+1,j+1) , helper(i,j+1) , helper(i+1,j) )

            return dp[(i,j)]
        dp={}
        return helper(0,0)
        