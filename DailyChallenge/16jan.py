# isme bas ye logic laga he xor of same numbers are 0
# ek chij imp he seekhne laayak isme ki if we want to not update the mapvalue then we use get 
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        count={}

        for n in nums1:
            count[n]=count.get(n,0)+len(nums2)
        for n in nums2:
            count[n]=count.get(n,0)+len(nums1)
        total=0
        for key,value in count.items():
            if value%2:
                total^=key
        return total
