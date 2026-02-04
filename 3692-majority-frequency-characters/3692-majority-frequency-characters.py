class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        sFreq = Counter(s)
        freqGroups = Counter([sFreq[k] for k in sFreq])
        majorFreqGroup = groupSize = 0

        for k, v in freqGroups.items():
            if v > groupSize:
                majorFreqGroup = k
                groupSize = v
            elif v == groupSize:
                majorFreqGroup = max(k, majorFreqGroup)
        
        res = [k for k, v in sFreq.items() if v == majorFreqGroup]
        
        return ''.join(res)