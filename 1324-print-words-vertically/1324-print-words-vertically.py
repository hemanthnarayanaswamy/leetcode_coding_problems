class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        ans=[]

        for i in range(max_len): # for each index
            toadd=""
            for word in words:  # Get the letter at each index
                if i<len(word):
                    toadd+=word[i]
                else:
                    toadd+=" "
            ans.append(toadd.rstrip(" "))
            
        return ans