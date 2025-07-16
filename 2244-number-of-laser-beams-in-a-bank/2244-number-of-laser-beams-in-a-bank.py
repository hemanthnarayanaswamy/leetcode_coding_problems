class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        numberDev = []
        lasers = 0

        for r in bank: # Create a Interger Array of number of devices per row ignoring zeros
            d = r.count('1')
            if d:
                numberDev.append(d)
        
        for i in range(len(numberDev)-1):
            lasers += numberDev[i] * numberDev[i+1]
        
        return lasers


        

        
