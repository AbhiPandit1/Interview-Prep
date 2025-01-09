# isme hume find no of ways nikalna he jisse hum reuqired coins bana skte h
# it is somehow similar to unbounded knapsack jime hume ek pura array dekh rhkha hota he weight nikalte he
# from amount in weight category aur jaise hi weight bdh jata he return krdete but if equal ho jata he weight then we
# send 1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def helper(i,total):
            if total>amount or i>=len(coins):
                return 0
            
            if total==amount:
                return 1
            if (i,amount) in dp:
                return dp[(i,total)]
            
            total_coins=0
            for j in range(i,len(coins)):
                if coins[j]+total<=amount:
                    total_coins+=helper(j,coins[j]+total)
            dp[(i,total)]=total_coins
            return dp[(i,total)]
        dp={}
        return helper(0,0)
            
            
            
        
        

