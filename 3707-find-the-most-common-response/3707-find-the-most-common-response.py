class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responsesFreq = Counter()
        commonRes = []

        for response in responses:
            responsesFreq.update(set(response))

        maxFreq = max(responsesFreq.values())
            
        return min((r for r,v in responsesFreq.items() if v == maxFreq))
