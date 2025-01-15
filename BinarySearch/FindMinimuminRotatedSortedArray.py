# rotate he simple binary seacrh and then check if our mid is bigger than nums[last]:
# if it tru shift the left to mid+1
# else our mid  j=mid and keep on search the smallest

class Solution:
    def findMin(self, nums: List[int]) -> int:

        i=0
        j=len(nums)-1

        while i<j:
            mid=i+(j-i)//2

            if nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid
        return nums[j]

