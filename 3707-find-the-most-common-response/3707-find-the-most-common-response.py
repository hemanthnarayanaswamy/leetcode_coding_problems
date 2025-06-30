class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responsesFreq = {}
        commonRes = []

        for i in range(len(responses)):
            uniqRes = set(responses[i])
            for r in uniqRes:
                responsesFreq[r] = responsesFreq.get(r, 0) + 1

        maxFreq = max(responsesFreq.values())

        for r,v in responsesFreq.items():
            if v == maxFreq:
                commonRes.append(r)

        return sorted(commonRes)[0]
