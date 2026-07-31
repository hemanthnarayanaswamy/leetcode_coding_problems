class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        freq1 = Counter(s1)
        freq2 = defaultdict(int)
        left = 0
       

        for right in range(len(s2)):
            freq2[s2[right]] += 1

            while right - left + 1 > n1:
                freq2[s2[left]] -= 1
                if not freq2[s2[left]]:
                    del freq2[s2[left]]
                left += 1
            
            if freq1 == freq2:
                return True  
        
        return False
