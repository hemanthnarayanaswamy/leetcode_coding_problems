class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            print('1')
            return False
        
        oddParity_s1 = []
        evenParity_s1 = []
        oddParity_s2 = []
        evenParity_s2 = []
        
        for i in range(len(s1)):
            if i % 2:
                oddParity_s1.append(s1[i])
                oddParity_s2.append(s2[i])
            else:
                evenParity_s1.append(s1[i])
                evenParity_s2.append(s2[i])
        
        if len(oddParity_s1) != len(oddParity_s2) or len(evenParity_s1) != len(evenParity_s2):
            print('2')
            return False
        
        if Counter(oddParity_s1) != Counter(oddParity_s2) or Counter(evenParity_s1) != Counter(evenParity_s2):
            print('3')
            return False
        
        return True