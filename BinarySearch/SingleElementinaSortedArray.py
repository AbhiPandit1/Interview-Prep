# kuch ni krna bas check for the element in even virtue while nums[i]==nums[i+1] keep on moving the mid by 2
# else right=mid-1
# return nums[l]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:


        l=0
        r=len(nums)-1

        while l<r:
            mid=l+(r-l)//2

            if mid%2:
                mid-=1
            
            if nums[mid]==nums[mid+1]:
                l=mid+2
            else:
                r=mid-1
        return nums[l]
        

        