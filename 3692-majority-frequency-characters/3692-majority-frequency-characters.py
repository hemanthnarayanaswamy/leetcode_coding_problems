class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counter = Counter(s)
        d = defaultdict(list)

        for ch, freq in counter.items():
            d[freq].append(ch)

        ans = max(d, key = lambda x: (len(d[x]), x)) 

        return ''.join(d[ans])
        