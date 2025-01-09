# isme hum text ke beech longest common sequence nikalna he 
# kuch ni krna keep a check if we reach at last of any of two we cant get any more sequence to we wrill return 0
# iske baad do cases honge if dono i pe aur j pe equal he to we will move to next
# else i ko move krwa ke dekhenge or j ko move krwa ke dekhenge and max of both

# Time Complexity--->O(m*n)
# Space Complexity--->O(m*n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def helper(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            
            

            if text1[i]==text2[j]:
                dp[(i,j)]=1+helper(i+1,j+1)
            else:
                dp[(i,j)]= max(helper(i,j+1),helper(i+1,j))
            return dp[(i,j)]
        
        dp={}
        
        return helper(0,0)
                