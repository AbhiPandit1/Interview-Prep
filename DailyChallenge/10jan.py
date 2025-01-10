# kuch ni krna max of freq of each word lelena he yehi bas thoda complex he 
# baki max leke isTrue ko initialise krna he compare krna he freq of ech word in word1
# if shi he to update krna he res ko

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        word2_max_count={}

        for word in words2:
            word2_count=Counter(word)
            for ch in word:
                word2_max_count[ch]=max(word2_max_count.get(ch,0), word2_count[ch])
        
        res=[]

    
        
        for word in words1:
            
            word1_count=Counter(word)
            isTrue=True

            for ch in word2_max_count:
                if word1_count[ch]<word2_max_count[ch]:
                    isTrue=False
            if isTrue:
                res.append(word)
        
        return res



        
    