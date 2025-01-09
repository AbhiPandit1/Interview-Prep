# Ye target sum ki trh lagega but in this we have to cosume whole array to hmara jo result aayega wo
# pure array pe hi aayega not on single to iske lie hume check krna he ki jo hmara array he uspe hum 
# plus lagayenge to kya hoga minus lagayenge to kya hoga and dono ka addition dena he as we need full
# array and for base case wo bb jab hum length ke equal honge tab check krna he

# Time Complexity will be len(nums)*target


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        def helper(i,total):
            if i>=len(nums):
                if total==target:
                    return 1
                return 0
            if (i,total) in dp:
                return dp[(i,total)]
            

            
            dp[(i,total)]= helper(i+1,total+nums[i]) + helper(i+1,total-nums[i])
            return dp[(i,total)]

        dp={}
        return helper(0,0)
