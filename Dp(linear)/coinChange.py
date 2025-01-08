# simple proble he unlimited coins he apne paas
# take and notTake use krna he 
# bas base case ka dhyaan rkhna he ki total agr jyda hojaaye amount se infinity send krna he
# kuki there is also cases we cant react to the amount 

#simple recursive approach
#Time complexity:O(2^n) as we are calling data for two parts everytime
#Space complexity:O(n) as we are using recursion stack

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def helper(i,total):

            if total>amount:
                return float("inf")
            
            if total==amount:
                return 0
            if (i,total) in dp:
                return dp[(i,total)]
            
            total_coins=float("inf")

            for j in range(i,len(coins)):
                total_coins=min(total_coins,1+helper(j,total+coins[j]))
            dp[(i,total)]= total_coins
            return dp[(i,total)]
        dp={}
        result=helper(0,0)

        return result if result != float("inf") else -1
