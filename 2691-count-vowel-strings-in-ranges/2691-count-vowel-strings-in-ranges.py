class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelCount = []
        count = 0
        n = len(queries)
        res = [0] * n
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            vowelCount.append(count)
        
        print(vowelCount)
          
        for i in range(n):
            l, r = queries[i][0], queries[i][1]
            if l == 0:
                res[i] = vowelCount[r] 
            else:
                res[i] = vowelCount[r] - vowelCount[l-1]
        
        return res


        

