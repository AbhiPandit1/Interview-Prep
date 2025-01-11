# iss question me hume pata krna he ki kya hum array ko k part me divide krskte he and all of them shoud be 
# palindrome so firts i though of partition dp  but it didnt worked 
# so ek simple solute he sabki frequency lelo and check if the odd no of frequency is less tha k



class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k==len(s):
            return True
        if k>len(s):
            return False
        count=Counter(s)
        count2=0

        for val,cnt in count.items():
            if cnt%2:
                count2+=1
        return count2<=k