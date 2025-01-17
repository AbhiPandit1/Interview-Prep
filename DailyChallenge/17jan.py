# it runs on the principle of o[i+1]=arr[i]^o[i] o[0]=0 if this is true return true 
# it runs on the principle of o[i+1]=arr[i]^o[i] o[0]=1 if this is true return true 
# return False

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        
        n=len(derived)
        original=[0]*n

        for i in range(len(derived)-1):
            original[i+1]=original[i]^derived[i]
        
        if original[n-1]^original[0]==derived[n-1]:
            return True
        
        original=[1]*n
        for i in range(len(derived)-1):
            original[i+1]=original[i]^derived[i]
        
        if original[n-1]^original[0]==derived[n-1]:
            return True
        
        return False
