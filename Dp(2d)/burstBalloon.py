# in burst balloon me hume ye chij dekhni he ki agar hum kisi balloon ko burst krte he to uske left and right me jo
# balloons he unka product nikalna he aur uske sath us balloon ko bhi add krna he
# isme hume ek chij dekhni he ki agar hume koi balloon burst krna he to uske left and right me koi balloon ni he to uska
# product 0 hoga isliye hume ek dummy balloon add krna he left and right me 1 and 1 ka
# iske bad hume ek dp bna lenge jisme hume left and right ka product store krna he
# coins=nums[i] + nums[left] +nums[right ] + helper(left,i) + helper(i,right)
#  max value nikal lena he

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def helper(left,right):
            if left+1==right:
                return 0
            if (left,right) in dp:
                return dp[(left,right)]
            

            max_coins=0

            for i in range(left+1,right):
                coins=nums[i]*nums[left]*nums[right]
                coins+=helper(left,i)+helper(i,right)
                max_coins=max(max_coins,coins)
            
            dp[(left,right)]= max_coins
            return dp[(left,right)]
        
        dp={}
        nums = [1] + nums + [1]

        
        return helper(0, len(nums) - 1)


