class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        tracker = defaultdict(list)
        res  = []
        
        for path in paths:
            tmp = path.split()
            parent = tmp[0]
            files = tmp[1:]

            for file in files:
                f,c = file.split('(')
                c = c[:-1]
                tracker[c].append(parent + '/' + f)
            
        for v in tracker.values():
            if len(v) > 1:
                res.append(v)

        return res


