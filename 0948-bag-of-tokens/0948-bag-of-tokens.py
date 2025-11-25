class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxScore = 0
        tmpScore = 0
        l, h = 0, len(tokens)-1

        while l <= h:
            if power >= tokens[l]:
                print("playing face up")
                tmpScore += 1
                power -= tokens[l]
                l += 1
                maxScore = max(maxScore, tmpScore)
            elif tmpScore:
                print("playing face down")
                power += tokens[h] 
                h -= 1
                tmpScore -= 1
            else:
                break
        
        return max(maxScore, tmpScore)