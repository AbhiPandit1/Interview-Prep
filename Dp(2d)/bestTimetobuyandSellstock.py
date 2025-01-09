#classic dp problem jisme hume stock ko maipulate krna he ki maximu profit paa ske
# the only thing is that ke ek din bechne ke baad hum uske agle din sell ni krskte


class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        def helper(i,buy):

            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            
            if buy:
                dp[(i,buy)]=max(helper(i+1,1),-prices[i]+helper(i+1,0))
            else:
                dp[(i,buy)]=max(helper(i+1,0),prices[i]+helper(i+2,1))
            
            return dp[(i,buy)]
        dp={}
        return helper(0,1)