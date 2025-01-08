# kuch ni krna check krna he sum divisible by 2 he ki ni if ni he to equla subsetme divide ni ho skta
# then target maan lena he sum/2 ko and the using memoized technieuq find krlena he
# sort krlena largest value ko phle dikhaane ke lie


class Solution:
    def canPartition(self, nums):

        total_sum=sum(nums)

        if total_sum%2:
            return False
        
        target=total_sum//2

        nums.sort()
        

        def helper(i,total):
            if total==target:
                return True
            if i>=len(nums) or total > target:
                return False
            if (i,total) in dp:
                return dp[(i,total)]
            
            take=helper(i+1,total+nums[i])

            notTake=helper(i+1,total)

            dp[(i,total)]= take or notTake
            return dp[(i,total)]
        
        dp={}
        
        return helper(0,0)
        