class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_range = [bin(int(field))[2:] for field in date.split('-')]
    
        return '-'.join(date_range)
            