class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxScore = 0
        score = 0
        low, high = 0, len(tokens)-1

        while low <= high:
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
                maxScore = max(maxScore, score)
            elif score:
                power += tokens[high] 
                high -= 1
                score -= 1
            else:
                break
        
        return max(maxScore, score)