<h2><a href="https://leetcode.com/problems/maximum-containers-on-a-ship">3817. Maximum Containers on a Ship</a></h2><h3>Easy</h3><hr><p>You are given a positive integer <code>n</code> representing an <code>n x n</code> cargo deck on a ship. Each cell on the deck can hold one container with a weight of <strong>exactly</strong> <code>w</code>.</p>

<p>However, the total weight of all containers, if loaded onto the deck, must not exceed the ship&#39;s maximum weight capacity, <code>maxWeight</code>.</p>

<p>Return the <strong>maximum</strong> number of containers that can be loaded onto the ship.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, w = 3, maxWeight = 15</span></p>

<p><strong>Output:</strong> 4</p>

<p><strong>Explanation: </strong></p>

<p>The deck has 4 cells, and each container weighs 3. The total weight of loading all containers is 12, which does not exceed <code>maxWeight</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, w = 5, maxWeight = 20</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation: </strong></p>

<p>The deck has 9 cells, and each container weighs 5. The maximum number of containers that can be loaded without exceeding <code>maxWeight</code> is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= w &lt;= 1000</code></li>
	<li><code>1 &lt;= maxWeight &lt;= 10<sup>9</sup></code></li>
</ul>

# Solution 
The problem requires us to determine the maximum number of containers that can be placed on an n x n cargo deck while ensuring the total weight does not exceed maxWeight.
* The deck can hold at most n * n containers.
* Each container has a weight of w, so the total weight of all k containers is k * w.
* The ship's weight limit maxWeight restricts how many containers can be placed.
* Thus, we take the minimum of n * n (the deck's maximum capacity) and maxWeight / w (the weight-constrained maximum).

## Approach 
1. Compute the total number of containers that the `n x n` deck can hold: `max_possible = n × n`
2. Compute the maximum number of containers that the ship can support under the weight constraint: `max_by_weight = ⌊maxWeight / w⌋`
3. Return the minimum of these two values: `result = min(max_possible, max_by_weight)`

```python
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cargoCells = n * n 
        possibleContainers = maxWeight // w 

        return min(cargoCells, possibleContainers)
```

```python
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return (n * n if n * n <= maxWeight // w else maxWeight // w)
```
