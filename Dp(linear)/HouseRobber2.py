# Recursive approach 
#isme kuch ni krna bas appko check hai ki jab bb outof bound ho jaaye to return 0 krna he ye to base case hogya
# hum  hume take notTake use krna he 
# for every prt we will have two option ya to le ya na le agr humne lia to hum uska agla ni leskte 
# islie hum function i+2 ke lie call krenge if we take and if not Take then for i+1
# and at last we will return the max of both
# but houserobber me we can can start from 0th index or 1stindex so we will take max of both
# but in houserobber2 hum nums se manipulate krenge and we as the last index is connected ith first means hum last 
#inde lete he to first ni leskte islie phle hum nums[1:] lenge nad the compare krenge nums[:len(nums)-1]
# jo bbmax hoga wo return krdenge but ek base case reh jaayega idhr jab only ek element ho arr me to hum arr[0] return krdenge


#Recursive Approach
#Time complexity: O(2^n)---->as we are calling data for two parts everytime
#space complexity:O(n)----> as we are using recursion stack

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(i,nums):
            if i>=len(nums):
                return 0
            
            
            return max(nums[i]+helper(i+2,nums),helper(i+1,nums))
        
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        return max(helper(0,nums[1:]),helper(0,nums[:len(nums)-1]))


#Memoized approach (ek chij ka dhyaan rkhna he done me dp alg leni he as it will contadict and we are comparing both of them)
class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(i,nums,dp):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            
            dp[i]=max(nums[i]+helper(i+2,nums,dp),helper(i+1,nums,dp))
            return dp[i]
        
        
        
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        return max(helper(0,nums[1:],{}),helper(0,nums[:len(nums)-1],{}))


# Iterative space optimized approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(start: int, end: int) -> int:
            prev2, prev1 = 0, 0
            for i in range(start, end):
                current = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = current
            return prev1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Case 1: Rob from house 1 to n-1 (exclude the first house)
        case1 = rob_range(1, n)
        
        # Case 2: Rob from house 0 to n-2 (exclude the last house)
        case2 = rob_range(0, n - 1)
        
        return max(case1, case2)

        