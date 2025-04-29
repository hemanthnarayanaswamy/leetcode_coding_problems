class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        scoreMap = {}

        for i in range(len(score)):
            scoreMap[score[i][k]] = score[i]

        # To get keys sorted by their values (descending):
        sorted_score = [v for k, v in sorted(scoreMap.items(), key=lambda item: item[0], reverse=True)]
       
        return sorted_score