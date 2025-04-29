class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        scoreMap = {}
        result = []

        for i in range(len(score)):
            scoreMap[score[i][k]] = score[i]

        sorted_scores = dict(sorted(scoreMap.items(), key=lambda item: item[0], reverse=True))
        
        for scr in sorted_scores.values():
            result.append(scr)
        
        return result