class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        header = set()
        orderDetails = defaultdict(lambda: defaultdict(int))
        tables = set()

        for order in orders:
            table = int(order[1])
            tables.add(table)
            for item in order[2:]:
                header.add(item)
                orderDetails[table][item] += 1
        
        header = ["Table"]+sorted(header)
        tables = sorted(tables)
        displayTable = [header]

        for t in tables:
            tmp = []
            tmp.append(str(t))
            for item in header[1:]:
                tmp.append(str(orderDetails[t][item]))
            displayTable.append(tmp)

        return displayTable 


