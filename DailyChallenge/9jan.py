
# easy question he prefix ka if word start with given prefix then we will increase the count
# thats it


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count=0

        for n in words:
            if n.startswith(pref):
                count+=1
        return count
        