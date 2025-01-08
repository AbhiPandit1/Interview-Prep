# decode ways me hume ek string dia hoga like 
# 26 isko hum do treeke se split krskte he 2 by taking single first value and if taking double then 26(2,6) and (26)
# 322 -(3,2,2) (32,2) (3,22) see we can divide into three part
# hume hume find krna he aisa hum kitni baar krskte he 

# so isme hum dekh skte he har ke baad hamare paas options he to take the firts varibale take both or move to second 
# but jab hum last me pchjyenge to ek rhega hi hmare paas so hum usko take krskte he and we will add one
# ye humara base case hoga
# now agr hume do digit saath me lena he to iske lie first digit ko ya to one hone chye ya 2 hone chye 
# but if 2 he first digit then hume make sure krna he ki jo third digit h wo 6 se chota ho kuki alphabet
# 26 se jyada thodi hoskte he

# so we will use recursive approach

# Time complexity:O(2^n) as we are calling data for two parts everytime
# space complexity:O(n) as we are using recursion stack
# memoized time complexity:O(n) as we are storing the data in dp sim

class Solution:
    def numDecodings(self, s: str) -> int:

        def helper(i):

            if i==len(s):
                return 1
            if s[i]=="0":
                return 0
            if i in dp:
                return dp[i]
            
            single=helper(i+1)

            double=0
            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and int(s[i+1])<=6):
                double=helper(i+2)
            
            dp[i]= single + double
            return dp[i]
        dp={}
        return helper(0)
            