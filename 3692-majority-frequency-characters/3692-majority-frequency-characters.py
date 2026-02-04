class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        sFreq = Counter(s)
        freqGroups = Counter([sFreq[k] for k in sFreq])
        majorFreqGroups = groupSize = 0

        for k, v in freqGroups.items():
            if v > groupSize:
                majorFreqGroups = k
                groupSize = v
            elif v == groupSize:
                majorFreqGroups = max(k, majorFreqGroups)
        
        res = [k for k, v in sFreq.items() if v == majorFreqGroups]
        
        return ''.join(res)