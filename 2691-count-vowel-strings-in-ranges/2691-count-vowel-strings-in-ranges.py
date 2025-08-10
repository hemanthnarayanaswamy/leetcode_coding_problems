class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelCount = [0]
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            vowelCount.append(count)
          
        res = []
        for l, r in queries:
            res.append(vowelCount[r + 1] - vowelCount[l])
        
        return res