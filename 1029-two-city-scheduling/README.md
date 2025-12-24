<h2><a href="https://leetcode.com/problems/two-city-scheduling">1095. Two City Scheduling</a></h2><h3>Medium</h3><hr><p>A company is planning to interview <code>2n</code> people. Given the array <code>costs</code> where <code>costs[i] = [aCost<sub>i</sub>, bCost<sub>i</sub>]</code>,&nbsp;the cost of flying the <code>i<sup>th</sup></code> person to city <code>a</code> is <code>aCost<sub>i</sub></code>, and the cost of flying the <code>i<sup>th</sup></code> person to city <code>b</code> is <code>bCost<sub>i</sub></code>.</p>

<p>Return <em>the minimum cost to fly every person to a city</em> such that exactly <code>n</code> people arrive in each city.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> costs = [[10,20],[30,200],[400,50],[30,20]]
<strong>Output:</strong> 110
<strong>Explanation: </strong>
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
<strong>Output:</strong> 1859
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
<strong>Output:</strong> 3086
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 * n == costs.length</code></li>
	<li><code>2 &lt;= costs.length &lt;= 100</code></li>
	<li><code>costs.length</code> is even.</li>
	<li><code>1 &lt;= aCost<sub>i</sub>, bCost<sub>i</sub> &lt;= 1000</code></li>
</ul>

# Wrong Attempt
* First seperate the `costA & costB`, sort them and take the minimum n values from each. 
```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        Acosts = [a for a, b in costs]
        Bcosts = [b for a, b in costs]
        Acosts.sort()
        Bcosts.sort()

        return sum(Acosts[:n] + Bcosts[:n])
```
1. The problem with this solution is that from `cost[i] = [a, b]`, we should only choose one among them, but from my solution if the min(a) or min(b) it is considered from the same cost sometimes which is wrong Implementation 

---
Imagine we didn't have the restriction that half the people need to go to A and the other half to B. How would you minimize the cost then? Easy, you would simply send each person to the location that minimizes their cost! Now, given this purely optimal assignment of people to locations, how could we modify this assignment to accomodate the restriction that half the people need to go to A and the other half to B?

# Intuition
If we sort people by the difference in `costs (A - B)`, it helps us determine:

* If `cost[i][0]` is much smaller than `cost[i][1]`, person i is better for `city A`.

* If `cost[i][0]` is much larger than `cost[i][1]`, person i is better for `city B`.

By sorting based on `(A - B)`, we ensure that the **first N people are cheaper for A**, and **the remaining N are cheaper for B**.

# Solution 
* We need to track the people left to sent to `city A & city B` i.e. `n`. 
* And We sort the `costs` array based on the absolute difference

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = b = len(costs) // 2
        sortedCosts = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        totalCost = 0

        for costA, costB in sortedCosts:
            if a and costA < costB:
                totalCost += costA
                a -= 1
            elif b and costB < costA:
                totalCost += costB
                b -= 1
            elif not a and costA < costB:
                totalCost += costB
                b -= 1
            else:
                totalCost += costA
                a -= 1
        
        return totalCost
```
* Instead of manually calculating and reducing `a and b`, we just need to assign first `n` to costA and then next `n` to costB, as its sorted by delta difference. 
* when we sort by `sorted(costs, key=lambda x: x[0] - x[1])`, values in the first `n` will have minimum `costA` (low diff values will be infront and large diff in last based on sort) --> **when we do `A-B`, If `A > B` diff will be more compared to `A < B`**

```ini
A = 20 B = 10 ( A > B)
A - B = 20 - 10 = 10 

A = 10  B = 20 
A - B = 10 - 20 =  -10

costs = [[10,20],[30,200],[400,50],[30,20]]
sorted(costs, key=lambda x: x[0] - x[1])
costs = [[30, 200], [10, 20], [30, 20], [400, 50]]
```
* In the above example you can see that for the first `n`, `CostA` is always `minimum`

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        sortedCosts = sorted(costs, key=lambda x: x[0] - x[1])  # Sort by cost difference (A - B)
        totalCost = 0
        print(sortedCosts)

        for costA, costB in sortedCosts:
            if n:
                totalCost += costA
                n -= 1
            else:
                totalCost += costB

        return totalCost
```
