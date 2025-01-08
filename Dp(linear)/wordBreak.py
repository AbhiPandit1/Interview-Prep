# isme kuch ninkrna just hume word break check krna he for s in the list
# wo if are reaching at last of s that means every word is present so this will be our base case
# the we will check for ever word in wordlist till i+len(word)<s and word[i:i+len(word)]==word
# then we will send it to explore other word dfs(i+len(word))
# and if we reach at the end then we will return True

#Space complexity:O(n)
#Time complexity:O(n^2)
#Memoized Time complexity:O(n*m)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def helper(i):
            if i>=len(s):
                return True
            

            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    if helper(i+len(word)):
                        dp[i]=True
                        return True
            dp[i]=False
            return False
        dp={}
        return helper(0)