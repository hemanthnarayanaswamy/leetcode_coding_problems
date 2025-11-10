<h2><a href="https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position">1329. Minimum Cost to Move Chips to The Same Position</a></h2><h3>Easy</h3><hr><p>We have <code>n</code> chips, where the position of the <code>i<sup>th</sup></code> chip is <code>position[i]</code>.</p>

<p>We need to move all the chips to <strong>the same position</strong>. In one step, we can change the position of the <code>i<sup>th</sup></code> chip from <code>position[i]</code> to:</p>

<ul>
	<li><code>position[i] + 2</code> or <code>position[i] - 2</code> with <code>cost = 0</code>.</li>
	<li><code>position[i] + 1</code> or <code>position[i] - 1</code> with <code>cost = 1</code>.</li>
</ul>

<p>Return <em>the minimum cost</em> needed to move all the chips to the same position.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg" style="width: 750px; height: 217px;" />
<pre>
<strong>Input:</strong> position = [1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg" style="width: 750px; height: 306px;" />
<pre>
<strong>Input:</strong> position = [2,2,2,3,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> position = [1,1000000000]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

# Solution 
**`Hint` : We can bring all the odd positioned coins at one odd place at cost 0 and similarly, we can bring all the even positioned coins at one even place at cost 0. After this, we just need to find whether we place odd to even or even to odd at the cost of min( odd, even);**

1. To Move the chips from `odd to odd` or `even to even`, the cost is zero `position[i] + 2 or position[i] - 2 with cost = 0`
2. But if you move to a different parit from anywhere else, the `cost=1`
3. Now counting all chips at even and odd while moving by keeping the moves zero. 
4. Now We need to move from the chips in from `even to odd/ odd to even` based on the minimum moves, 
5. The cost to moving all the chips `n` from `odd to even/ even to odd` is n.
6. So we need to find the minimum cost, the the minimum cost is to move the the chips with minimum count into other. 

```python
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips_even = 0
        chips_odd = 0

        for p in position:
            if p % 2:
                chips_odd += 1
            else:
                chips_even += 1
        
        return min(chips_even, chips_odd)
```

## Approach
* Identify Parity:
Chips at even positions can be moved amongst each other at no cost, similarly for odd positions due to the zero-cost of two-position moves.
The only time a cost is incurred is when moving a chip from an even position to an odd position, or vice versa, as this requires a one-position move.
* Count Parity:
Iterate through the array of chip positions.
Maintain two counters: one for chips at even positions (evenCount) and another for chips at odd positions (oddCount).
* Calculate Minimum Cost:
Since moving chips within the same parity group (even to even or odd to odd) costs nothing, the only decision is to determine the lesser cost between moving all even-positioned chips to an odd position or moving all odd-positioned chips to an even position.
The cost is directly proportional to the number of chips being moved. Hence, to minimize the cost, you would move all chips from the smaller group (either oddCount or evenCount) to the larger group.
* Return the Result:
The function returns the smaller of the two counts (evenCount or oddCount), representing the minimum cost based on the number of moves required.
<ul>
	<li><code>1 &lt;= position.length &lt;= 100</code></li>
	<li><code>1 &lt;= position[i] &lt;= 10^9</code></li>
</ul>
