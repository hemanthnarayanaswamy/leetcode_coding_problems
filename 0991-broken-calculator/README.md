<h2><a href="https://leetcode.com/problems/broken-calculator">1033. Broken Calculator</a></h2><h3>Medium</h3><hr><p>There is a broken calculator that has the integer <code>startValue</code> on its display initially. In one operation, you can:</p>

<ul>
	<li>multiply the number on display by <code>2</code>, or</li>
	<li>subtract <code>1</code> from the number on display.</li>
</ul>

<p>Given two integers <code>startValue</code> and <code>target</code>, return <em>the minimum number of operations needed to display </em><code>target</code><em> on the calculator</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> startValue = 2, target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Use double operation and then decrement operation {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> startValue = 5, target = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> Use decrement and then double {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> startValue = 3, target = 10
<strong>Output:</strong> 3
<strong>Explanation:</strong> Use double, decrement and double {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= startValue, target &lt;= 10<sup>9</sup></code></li>
</ul>

# Solution
1. We have two operations, multiple and subtract

```ini
We reverse the problem, we'll make the target match the startValue

Operations used will become
- diviide 
- add
```
### `Condition1: target > startValue`
- if `target` is odd we increase `target += 1`
- if `target` is even and `target is greater than startValue`, we'll half target `target //= 2`

### `Condition2: target < startValue`
- only thing to do is increace `target` by one until we reach `startValue`, so the number moves will be `moves += (startValue - target)`

```python
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        moves = 0

        while target != startValue:
            if target < startValue:
                moves += startValue - target
                break
                
            # Assuming that target needs to be reduced to match startValue
            if target % 2 == 0 and target > startValue:
                target //= 2
            else:
                target += 1
            moves += 1

        return moves
```

