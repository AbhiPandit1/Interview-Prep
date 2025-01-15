# do binary search banege phla if result found to right mid-1 krdena ki left mid-1 me seacrh krne ke lie
# dusra left=mid+1 krdena he mid+1 se right tak search krne ke lie and if found ans usko rkh lena
# he apne variable se jo initialize hoga -1,-1 se

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first():

            left=0
            right=len(nums)-1
            first=-1

            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]==target:
                    first=mid
                    right=mid-1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return first
        def second():

            left=0
            right=len(nums)-1
            second=-1

            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]==target:
                    second=mid
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return second
        
        first=first()
        second=second()
        return [first,second]