class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        n1 = len(s1)
        n2 = len(s2)

        # We make s1 is longer and s2 is shorter string
        if n1 < n2:
            s1, s2 = s2, s1
            n1, n2 = n2, n1
        
        left = 0
        right1 = n1-1
        right2 = n2-1

        while left < n2 and s1[left] == s2[left]:
            left += 1
        
        while right2 >= 0 and s1[right1] == s2[right2]:
            right1 -= 1
            right2 -= 1
        
        if left > right2: 
            return True
        else:
            return False
