<h2><a href="https://leetcode.com/problems/jewels-and-stones">782. Jewels and Stones</a></h2><h3>Easy</h3><hr><p>You&#39;re given strings <code>jewels</code> representing the types of stones that are jewels, and <code>stones</code> representing the stones you have. Each character in <code>stones</code> is a type of stone you have. You want to know how many of the stones you have are also jewels.</p>

<p>Letters are case sensitive, so <code>&quot;a&quot;</code> is considered a different type of stone from <code>&quot;A&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> jewels = "aA", stones = "aAAbbbb"
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> jewels = "z", stones = "ZZ"
<strong>Output:</strong> 0
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;jewels.length, stones.length &lt;= 50</code></li>
	<li><code>jewels</code> and <code>stones</code> consist of only English letters.</li>
	<li>All the characters of&nbsp;<code>jewels</code> are <strong>unique</strong>.</li>
</ul>

## Solution Approach 
* Count the Stones Frequency
* For each jewel add the freq of that jewel in stones

```python
from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        count = 0

        for jewel in jewels:
            count += stones.get(jewel, 0)
        
        return count
```

## Optimal Solution

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        d1 = defaultdict(int)
				
        for i in jewels:    # Start a deafult dict and initial all jewel elements val to zero
            d1[i] = 0
						
        for i in stones:
            if i in d1:   # If stone is a jewel add one
                d1[i]+=1
        return sum(d1.values())   # Return sum of default dict that stones the occuance of jewel in stones
```
