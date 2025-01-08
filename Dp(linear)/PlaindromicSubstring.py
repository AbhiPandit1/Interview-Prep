# is question me max length ke substring ko identify krna he in a given string
# so we will use brute force in brute force technique we will find every substring and then 
#check it for palindromic and update the maxlength as required and update our result string 
# if max_length is change an dthen return it
#Count substring
# same as above just have to give the count of substring


#Brute force approach 
#Time complexity:O(n^3) as we are checking every substring
#Space complexity:O(1) as we are not using any extra space
class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_length=0
        res=""

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if len(s[i:j])>max_length:
                        max_length=len(s[i:j])
                        res=s[i:j]

                        
        
        return res

