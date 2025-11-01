class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = defaultdict(Counter)   # table -> {food: count}
        foods = set()

        for _, table, food in orders:   # each order has one food
            t = int(table)
            tables[t][food] += 1
            foods.add(food)

        food_list = sorted(foods)
        out = [["Table"] + food_list]
        for t in sorted(tables):
            c = tables[t]
            out.append([str(t)] + [str(c[f]) for f in food_list])
        return out