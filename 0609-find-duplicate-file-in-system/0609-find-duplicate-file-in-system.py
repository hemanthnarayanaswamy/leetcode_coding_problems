class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content = defaultdict(list)
        res  = []
        
        for file in paths:
            tmp = file.split()
            parent = tmp[0]

            for c in tmp[1:]:
                x,y = c.split('(')
                y = y[:-1]
                content[y].append(parent + '/' + x)
            
        for path in content.values():
            if len(path) > 1:
                res.append(path)

        return res


