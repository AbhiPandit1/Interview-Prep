# main thought process he star ko kaise hanfle kre
# if s[i]==s[j] ho aur ya p[j]=="." to bina soche hum dono ko aage bdha skte he check case daal den ki i<len(s) hona chye
# ab dusra jab p[j]=="*" ho to ab do case handle krna hoga 
# ek to noTake wala jab hum * ko ni lenge j move krjyega aage i wohi rhega
# if take lenge to i+2 hojyega kuki * ka ek bhi lena he and preceeding se match hogya ye bb checkkrenge isme

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def helper(i,j):
            if i==len(s) and j==len(p):
                return True
            
            if j==len(p):
                return False
            
            isMatch = i<len(s) and ( s[i]== p[j] or p[j]==".")

            if j+1<len(p) and p[j+1]=="*":
                notTake=helper(i,j+2)
                take= isMatch and helper(i+1,j)
                return take or notTake
            else:
                return isMatch and helper(i+1,j+1)
        
        return helper(0,0)
                