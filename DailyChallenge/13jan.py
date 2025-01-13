# some operation we can do like we are on i and there is same value as s[i] in left and s[i] in right
# then we need to delete closest 

# so imple soln he freq  count krte rehna he jaise hi koi value 3 ke equal pche do subtract krdo
# and return count.values()

class Solution:
    def minimumLength(self, s: str) -> int:

        count={}


        for i in range(len(s)):

            count[s[i]]=1+count.get(s[i],0)
            if count[s[i]]==3:
                count[s[i]]-=2
        return sum(count.values())
       