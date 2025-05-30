<h2><a href="https://leetcode.com/problems/maximum-ice-cream-bars">1961. Maximum Ice Cream Bars</a></h2><h3>Medium</h3><hr><p>It is a sweltering summer day, and a boy wants to buy some ice cream bars.</p>

<p>At the store, there are <code>n</code> ice cream bars. You are given an array <code>costs</code> of length <code>n</code>, where <code>costs[i]</code> is the price of the <code>i<sup>th</sup></code> ice cream bar in coins. The boy initially has <code>coins</code> coins to spend, and he wants to buy as many ice cream bars as possible.&nbsp;</p>

<p><strong>Note:</strong> The boy can buy the ice cream bars in any order.</p>

<p>Return <em>the <strong>maximum</strong> number of ice cream bars the boy can buy with </em><code>coins</code><em> coins.</em></p>

<p>You must solve the problem by counting sort.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> costs = [1,3,2,4,1], coins = 7
<strong>Output:</strong> 4
<strong>Explanation: </strong>The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> costs = [10,6,8,7,7,8], coins = 5
<strong>Output:</strong> 0
<strong>Explanation: </strong>The boy cannot afford any of the ice cream bars.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> costs = [1,6,3,1,2,5], coins = 20
<strong>Output:</strong> 6
<strong>Explanation: </strong>The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>costs.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= costs[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coins &lt;= 10<sup>8</sup></code></li>
</ul>

# Solution 
- Key Observations:
* Sorting the costs in ascending order ensures that we start with the cheapest options.
* Using counting sort is beneficial since the cost values are small (bounded by constraints).
* Keep subtracting the cost of each ice cream from coins until there are no more coins left.

-----------------------------------------------------------------------------------------------------------------
* Use the Normal Sorting mentod to solve it.

```python
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bars = 0
        costs.sort()
        
        for cost in costs: 
            if cost <= coins:
                bars += 1
                coins -= cost
        
        return bars
```

## Optimal Solution
1. Use Counting Sort for Optimization
      * Instead of sorting directly (which takes O(n log n)), use counting sort since cost values are within a small range.
      * Create a frequency array to store the count of each cost value.
      * Construct a sorted list from the frequency array.
```python
