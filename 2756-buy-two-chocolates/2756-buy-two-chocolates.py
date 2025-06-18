class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        firstCho, secondCho = float(inf), float(inf)

        for p in prices:
            if p < firstCho:
                secondCho = firstCho 
                firstCho = p 
            elif p < secondCho:
                secondCho = p
        
        choPrice = firstCho + secondCho
        
        return money if choPrice > money else money - choPrice
