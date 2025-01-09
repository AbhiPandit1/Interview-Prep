# isme hume subsequence dekhna he ki kaise hum s ko t me bna skte he 
# iske lie hume do cases dekhne honge ki agar dono equal he to hum dono ko move kr denge
# agar equal ni he to hume ek ko move krna he and ek ko waise hi rkna he
# base case hoga agr hum t ke equal pch gye to return 1 krenge and s ke end pe pch gye to return 0

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def helper(i,j):

            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            if s[i]==t[j]:
                dp[(i,j)]=helper(i+1,j+1) + helper(i+1,j)
            else:
                dp[(i,j)]=helper(i+1,j)
            return dp[(i,j)]
        dp={}
        return helper(0,0)
            
            
