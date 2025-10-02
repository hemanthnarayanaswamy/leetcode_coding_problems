<h2><a href="https://leetcode.com/problems/water-bottles-ii">3336. Water Bottles II</a></h2><h3>Medium</h3><hr><p>You are given two integers <code>numBottles</code> and <code>numExchange</code>.</p>

<p><code>numBottles</code> represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:</p>

<ul>
	<li>Drink any number of full water bottles turning them into empty bottles.</li>
	<li>Exchange <code>numExchange</code> empty bottles with one full water bottle. Then, increase <code>numExchange</code> by one.</li>
</ul>

<p>Note that you cannot exchange multiple batches of empty bottles for the same value of <code>numExchange</code>. For example, if <code>numBottles == 3</code> and <code>numExchange == 1</code>, you cannot exchange <code>3</code> empty water bottles for <code>3</code> full bottles.</p>

<p>Return <em>the <strong>maximum</strong> number of water bottles you can drink</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/28/exampleone1.png" style="width: 948px; height: 482px; padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>Input:</strong> numBottles = 13, numExchange = 6
<strong>Output:</strong> 15
<strong>Explanation:</strong> The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/28/example231.png" style="width: 990px; height: 642px; padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>Input:</strong> numBottles = 10, numExchange = 3
<strong>Output:</strong> 13
<strong>Explanation:</strong> The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numBottles &lt;= 100 </code></li>
	<li><code>1 &lt;= numExchange &lt;= 100</code></li>
</ul>

# Solution
## Problem Logic:
* Start with `numBottles` full bottles
* Drink all bottles → get same number of empty bottles
* Exchange `numExchange` empty bottles for 1 new full bottle
After each exchange, `numExchange` increases by 1
Repeat until not enough empty bottles to exchange

## Algorithm Steps:
1. Initialize: `bottlesDrunk = emptyBottles = numBottles`
2. While `emptyBottles >= numExchange`:
		* Use `numExchange` empty bottles → get 1 new bottle
		* Drink the new bottle → `bottlesDrunk++`, `emptyBottles++`
		* Increase `exchange rate → numExchange++`
		* Remove used `empty bottles → emptyBottles -= numExchange`
		
## Key Insight:
* Each exchange gives 1 new bottle to drink
* Exchange cost increases each time (gets harder)
* Track total bottles drunk, not just exchanges

```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = emptyBottles = numBottles 

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange - 1
            numExchange += 1
            bottlesDrunk += 1

        return bottlesDrunk
```
---
```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = emptyBottles = numBottles 

        while emptyBottles >= numExchange:
            emptyBottles += 1 - numExchange  # +1 new empty, -numExchange used
            numExchange += 1
            bottlesDrunk += 1

        return bottlesDrunk
```
