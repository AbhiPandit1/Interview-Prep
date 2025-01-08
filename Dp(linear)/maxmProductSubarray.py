# isme hume subaarray ka max product batana he
# take prefix from starting and suffix from end
# if prefix==0 then we will reinitialise it to 1 similarly for suffix
# then we will take max of prfix and suffix and update the product 

#Time complexity:O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        product=float("-inf")
        suffix=1
        prefix=1

        for i in range(len(nums)):

            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix*=nums[i]
            suffix*=nums[len(nums)-i-1]

            product=max(product,max(prefix,suffix))
        
        return product

