# simple bas max(str1,str2) tak go throught
# then if put a check condition i<len(str1) he to tem+=str1[i] viceversa


class Solution(object):
    def mergeAlternately(self, word1, word2):
        temp=""
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                temp+=word1[i]
            if i<len(word2):
                temp+=word2[i]
        return str(temp)
            

