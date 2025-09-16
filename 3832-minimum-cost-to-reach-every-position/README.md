<h2><a href="https://leetcode.com/problems/minimum-cost-to-reach-every-position">3832. Minimum Cost to Reach Every Position</a></h2><h3>Easy</h3><hr><p data-end="438" data-start="104">You are given an integer array <code data-end="119" data-start="113">cost</code> of size <code data-end="131" data-start="128">n</code>. You are currently at position <code data-end="166" data-start="163">n</code> (at the end of the line) in a line of <code data-end="187" data-start="180">n + 1</code> people (numbered from 0 to <code data-end="218" data-start="215">n</code>).</p>

<p data-end="438" data-start="104">You wish to move forward in the line, but each person in front of you charges a specific amount to <strong>swap</strong> places. The cost to swap with person <code data-end="375" data-start="372">i</code> is given by <code data-end="397" data-start="388">cost[i]</code>.</p>

<p data-end="487" data-start="440">You are allowed to swap places with people as follows:</p>

<ul data-end="632" data-start="488">
	<li data-end="572" data-start="488">If they are in front of you, you <strong>must</strong> pay them <code data-end="546" data-start="537">cost[i]</code> to swap with them.</li>
	<li data-end="632" data-start="573">If they are behind you, they can swap with you for free.</li>
</ul>

<p data-end="755" data-start="634">Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong data-end="680" data-start="664">minimum</strong> total cost to reach each position <code>i</code> in the line<font face="monospace">.</font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">cost = [5,3,4,1,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[5,3,3,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>We can get to each position in the following way:</p>

<ul>
	<li><code>i = 0</code>. We can swap with person 0 for a cost of 5.</li>
	<li><span class="example-io"><code><font face="monospace">i = </font>1</code>. We can swap with person 1 for a cost of 3.</span></li>
	<li><span class="example-io"><code>i = 2</code>. We can swap with person 1 for a cost of 3, then swap with person 2 for free.</span></li>
	<li><span class="example-io"><code>i = 3</code>. We can swap with person 3 for a cost of 1.</span></li>
	<li><span class="example-io"><code>i = 4</code>. We can swap with person 3 for a cost of 1, then swap with person 4 for free.</span></li>
	<li><span class="example-io"><code>i = 5</code>. We can swap with person 3 for a cost of 1, then swap with person 5 for free.</span></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">cost = [1,2,4,6,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>We can swap with person 0 for a cost of <span class="example-io">1, then we will be able to reach any position <code>i</code> for free.</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == cost.length &lt;= 100</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 100</code></li>
</ul>

# Solution 
The problem is is equivalent to this problem: For each element in cost, determine the minimum value in costs preceding that element.
* After you swap with someone, they move behind you. This means once you've paid to swap with someone, you can later swap with people they were in front of for free.
```python
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        res= [0] * n
        prefixMin = 100

        for i in range(n):
            res[i] = min(prefixMin, cost[i])
            prefixMin = res[i]
        
        return res
```

* With cost = `[5,3,4,1,3,2]`:

Starting at position 6 (end of line), people are at positions 0-5: `0 1 2 3 4 5 Y(6)`
* Position 0: Pay person 0 directly (cost 5) = total 5
* Position 1: Pay person 1 directly (cost 3) = total 3
* Position 2: First get to position 1 (cost 3), then person 2 can swap with you for free = total 3
* Position 3: Pay person 3 directly (cost 1) = total 1
* Position 4: First get to position 3 (cost 1), then person 4 can swap with you for free = total 1
* Position 5: First get to position 3 (cost 1), then person 5 can swap with you for free = total 1

The free swap rule means that once you're at position `i`, any person at position `j > i` can swap with you for free because they're behind you. 
This is why after getting to position 3, we can get to positions 4 and 5 without additional cost.

This gives us `[5, 3, 3, 1, 1, 1]` which matches the expected output.

```python
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        a=float('inf')
        ans=[]
        for i in range(len(cost)):
            if cost[i]<=a:
                a=cost[i]
            ans.append(a)
        return ans
```
