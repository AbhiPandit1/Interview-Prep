# do string he usse hume thried string banana he just only condition is this ki done
# ka order same hona chye 
# iske lie base case hoga ki hum apne s1 ke aur s2 ke end me pche to we can return true
# we cancheck if i<len(s1) and j<len(s2) and k<len(s3) and s1[i]==s3[k] and s2[j]==s3[k]
# return True


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False

        def helper(i,j):
            if i==len(s1) and j==len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            result = False
            if i<len(s1) and s1[i]==s3[i+j]:
               result =result or helper(i+1,j)
            if j<len(s2) and s2[j]==s3[i+j]:
                result=result or helper(i,j+1)
            dp[(i,j)]=result
            return dp[(i,j)]
        dp={}
        return helper(0,0)


        