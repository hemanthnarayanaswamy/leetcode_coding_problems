class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        sFreq = Counter(s)
        freq = [v for v in sFreq.values()]
        freqGroups = Counter(freq)
        majorityGroup = 0
        groupSize = 0

        for k, v in freqGroups.items():
            if v > groupSize:
                majorityGroup = k
                groupSize = v
            elif v == groupSize:
                majorityGroup = max(k, majorityGroup)
        
        res = ''
        for k, v in sFreq.items():
            if v == majorityGroup:
                res += k
                
        return res