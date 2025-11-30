class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validCoupons = defaultdict(list)
        business = {"electronics", "grocery", "pharmacy", "restaurant"}
        res = []

        for c,b,a in zip(code, businessLine, isActive):
            print(a)
            if c and c.replace('_', 'a').isalnum() and a and (b in business):
                validCoupons[b].append(c)
        
        sortedValidCoupons = sorted(validCoupons.items())
        
        for _, v in sortedValidCoupons:
            v.sort()
            res.extend(v)
        
        return res