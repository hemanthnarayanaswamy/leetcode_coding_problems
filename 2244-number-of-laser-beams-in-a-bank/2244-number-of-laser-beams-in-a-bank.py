class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        numberDev = []
        lasers = 0
        x = bank[0].count('1')

        for i in range(1, len(bank)): 
            y = bank[i].count('1')
            if y:
                lasers += x * bank[i].count('1')
                x = y
        
        return lasers


        

        
