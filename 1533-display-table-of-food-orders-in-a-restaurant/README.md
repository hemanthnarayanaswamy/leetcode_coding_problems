<h2><a href="https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant">1533. Display Table of Food Orders in a Restaurant</a></h2><h3>Medium</h3><hr><p>Given&nbsp;the array <code>orders</code>, which represents the orders that customers have done in a restaurant. More specifically&nbsp;<code>orders[i]=[customerName<sub>i</sub>,tableNumber<sub>i</sub>,foodItem<sub>i</sub>]</code> where <code>customerName<sub>i</sub></code> is the name of the customer, <code>tableNumber<sub>i</sub></code>&nbsp;is the table customer sit at, and <code>foodItem<sub>i</sub></code>&nbsp;is the item customer orders.</p>

<p><em>Return the restaurant&#39;s &ldquo;<strong>display table</strong>&rdquo;</em>. The &ldquo;<strong>display table</strong>&rdquo; is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is &ldquo;Table&rdquo;, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> orders = [[&quot;David&quot;,&quot;3&quot;,&quot;Ceviche&quot;],[&quot;Corina&quot;,&quot;10&quot;,&quot;Beef Burrito&quot;],[&quot;David&quot;,&quot;3&quot;,&quot;Fried Chicken&quot;],[&quot;Carla&quot;,&quot;5&quot;,&quot;Water&quot;],[&quot;Carla&quot;,&quot;5&quot;,&quot;Ceviche&quot;],[&quot;Rous&quot;,&quot;3&quot;,&quot;Ceviche&quot;]]
<strong>Output:</strong> [[&quot;Table&quot;,&quot;Beef Burrito&quot;,&quot;Ceviche&quot;,&quot;Fried Chicken&quot;,&quot;Water&quot;],[&quot;3&quot;,&quot;0&quot;,&quot;2&quot;,&quot;1&quot;,&quot;0&quot;],[&quot;5&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;],[&quot;10&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]] 
<strong>Explanation:
</strong>The displaying table looks like:
<strong>Table,Beef Burrito,Ceviche,Fried Chicken,Water</strong>
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders &quot;Ceviche&quot; and &quot;Fried Chicken&quot;, and Rous orders &quot;Ceviche&quot;.
For the table 5: Carla orders &quot;Water&quot; and &quot;Ceviche&quot;.
For the table 10: Corina orders &quot;Beef Burrito&quot;. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> orders = [[&quot;James&quot;,&quot;12&quot;,&quot;Fried Chicken&quot;],[&quot;Ratesh&quot;,&quot;12&quot;,&quot;Fried Chicken&quot;],[&quot;Amadeus&quot;,&quot;12&quot;,&quot;Fried Chicken&quot;],[&quot;Adam&quot;,&quot;1&quot;,&quot;Canadian Waffles&quot;],[&quot;Brianna&quot;,&quot;1&quot;,&quot;Canadian Waffles&quot;]]
<strong>Output:</strong> [[&quot;Table&quot;,&quot;Canadian Waffles&quot;,&quot;Fried Chicken&quot;],[&quot;1&quot;,&quot;2&quot;,&quot;0&quot;],[&quot;12&quot;,&quot;0&quot;,&quot;3&quot;]] 
<strong>Explanation:</strong> 
For the table 1: Adam and Brianna order &quot;Canadian Waffles&quot;.
For the table 12: James, Ratesh and Amadeus order &quot;Fried Chicken&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> orders = [[&quot;Laura&quot;,&quot;2&quot;,&quot;Bean Burrito&quot;],[&quot;Jhon&quot;,&quot;2&quot;,&quot;Beef Burrito&quot;],[&quot;Melissa&quot;,&quot;2&quot;,&quot;Soda&quot;]]
<strong>Output:</strong> [[&quot;Table&quot;,&quot;Bean Burrito&quot;,&quot;Beef Burrito&quot;,&quot;Soda&quot;],[&quot;2&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;orders.length &lt;= 5 * 10^4</code></li>
	<li><code>orders[i].length == 3</code></li>
	<li><code>1 &lt;= customerName<sub>i</sub>.length, foodItem<sub>i</sub>.length &lt;= 20</code></li>
	<li><code>customerName<sub>i</sub></code> and <code>foodItem<sub>i</sub></code> consist of lowercase and uppercase English letters and the space character.</li>
	<li><code>tableNumber<sub>i</sub>&nbsp;</code>is a valid integer between <code>1</code> and <code>500</code>.</li>

</ul>

# Approach 
**`defaultdict` with nested dict with different types**
```python
from collections import defaultdict
d = defaultdict(lambda: defaultdict(int))
```
* This will create a new `defaultdict(int)` whenever a new key is accessed in `d`, 

```python
a = [("key1", {"a1":22, "a2":33}),
     ("key2", {"a1":32, "a2":55}),
     ("key3", {"a1":43, "a2":44})]
```
---

```python
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
```
---
# Optimal Solution 
	1. `tables = defaultdict(Counter)`: maps table → counts of each food.
	2. `foods = set()`: collects all distinct food names.
	3.	For each `order (_, table, food)`:
	4. Increment `tables[table][food] += 1`. Add food to foods.
	5. Sort foods to define the column order. Sort table numbers for row order.
	6. Build `header ["Table"] + sorted_foods`.
	7. For each table, `emit [str(table)] + [str(count[food])` for food in sorted_foods].
	8. Missing foods default to 0 because Counter returns 0 for unseen keys.
	
```python
from collections import defaultdict, Counter
from typing import List

def displayTable(orders):
    tables = defaultdict(Counter)   # table -> {food: count}
    foods = set()

    for _, table, food in orders:   # each order has one food
        print(table, food) # 3 Ceviche, 10 Beef Burrito, 3 Fried Chicken, 5 Ceviche
        t = int(table)
        tables[t][food] += 1
        foods.add(food)
    
    print(tables) # defaultdict(<class 'collections.Counter'>, {3: Counter({'Ceviche': 2, 'Fried Chicken': 1}), 10: Counter({'Beef Burrito': 1}), 5: Counter({'Water': 1, 'Ceviche': 1})})

    food_list = sorted(foods)
    out = [["Table"] + food_list]
    for t in sorted(tables):
        c = tables[t]
        out.append([str(t)] + [str(c[f]) for f in food_list])
    return out
```
