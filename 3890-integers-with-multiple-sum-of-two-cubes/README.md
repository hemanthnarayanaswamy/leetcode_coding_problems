<h2><a href="https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes">4268. Integers With Multiple Sum of Two Cubes</a></h2><h3>Medium</h3><hr><p>You are given an integer <code>n</code>.</p>

<p>An integer <code>x</code> is considered <strong>good</strong> if there exist <strong>at least</strong> two <strong>distinct</strong> pairs <code>(a, b)</code> such that:</p>

<ul>
	<li><code>a</code> and <code>b</code> are positive integers.</li>
	<li><code>a &lt;= b</code></li>
	<li><code>x = a<sup>3</sup> + b<sup>3</sup></code></li>
</ul>

<p>Return an array containing all good integers <strong>less than or equal to</strong> <code>n</code>, sorted in ascending order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4104</span></p>

<p><strong>Output:</strong> <span class="example-io">[1729,4104]</span></p>

<p><strong>Explanation:</strong></p>

<p>Among integers less than or equal to 4104, the good integers are:</p>

<ul>
	<li>1729: <code>1<sup>3</sup> + 12<sup>3</sup> = 1729</code> and <code>9<sup>3</sup> + 10<sup>3</sup> = 1729</code>.</li>
	<li>4104: <code>2<sup>3</sup> + 16<sup>3</sup> = 4104</code> and <code>9<sup>3</sup> + 15<sup>3</sup> = 4104</code>.</li>
</ul>

<p>Thus, the answer is <code>[1729, 4104]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 578</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no good integers less than or equal to 578, so the answer is an empty array.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


### Definition of a good integer
- An integer x is considered good only if:

There exist at least two distinct pairs `(a,b)` such that
• `a` and `b` are positive integers
• `a≤b` 
• `x = a^3 + b^3`
✅ The key phrase is `at least two distinct pairs`.

```ini
Why 9 = 1³ + 2³ is NOT a good integer

There is no second, different pair (a,b) that also gives 9.
9 is NOT a good integer
```
## Approach
* Use a `map` to count how many times each value of a3 + b3 appears. A value is good if it can be formed by at least two distinct pairs. Collect all such values and return them in sorted order

## Solution
```python
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        freq = defaultdict(int)

        for i in range(n):
            for j in range(i, n):
                tmp = i**3 + j**3
                if tmp <= n:
                    freq[tmp] += 1        
        
        res = []
        
        for num, f in freq.items():
            if f > 1:
                res.append(num)
        
        return sorted(res)
```
* Too many iterations, need to reduce the range (use n^1/3)
* Break the first loop is `i**3 > n`
* Can I stop computing further b values once a³ + b³ > n for fixed a? **Break second loop when x > n**
* No need seperate loop for freq and not need to add `+= 1` everytime and don't need to add duplicates.

```python
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        freq = defaultdict(int)
        limit = int(n**(1/3)) + 1
        res = set()

        for i in range(1, limit):
            a = i ** 3
            if a >= n:
                break
            for j in range(i, limit):
                b = j ** 3
                x = a + b
                if x <= n:
                    if x in freq and x not in res:
                        res.add(x)
                    else:
                        freq[x] = 1  
                else:
                    break       
        
        return sorted(res)
```
