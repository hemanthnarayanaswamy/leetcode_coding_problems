class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        
        for i in range(len(operations)):
            ops = operations[i]
            if ops == 'D':
                score.append(score[-1]*2)
            elif ops == 'C':
                score.pop()
            elif ops == '+':
                score.append(score[-2]+score[-1])
            else:
                score.append(int(ops))
        
        return sum(score)
            