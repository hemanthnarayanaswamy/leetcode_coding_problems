<h2><a href="https://leetcode.com/problems/di-string-match">979. DI String Match</a></h2><h3>Easy</h3><hr><p>A permutation <code>perm</code> of <code>n + 1</code> integers of all the integers in the range <code>[0, n]</code> can be represented as a string <code>s</code> of length <code>n</code> where:</p>

<ul>
	<li><code>s[i] == &#39;I&#39;</code> if <code>perm[i] &lt; perm[i + 1]</code>, and</li>
	<li><code>s[i] == &#39;D&#39;</code> if <code>perm[i] &gt; perm[i + 1]</code>.</li>
</ul>

<p>Given a string <code>s</code>, reconstruct the permutation <code>perm</code> and return it. If there are multiple valid permutations perm, return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "IDID"
<strong>Output:</strong> [0,4,1,3,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "III"
<strong>Output:</strong> [0,1,2,3]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "DDI"
<strong>Output:</strong> [3,2,0,1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;I&#39;</code> or <code>&#39;D&#39;</code>.</li>
</ul>


# Solution Approach 
* Initiate a Incremental and a DECREMENTAL value `0, len(s)` 
* Whenever `I` is found append the Incremental Value and Increement it by one for next iterastion 
* Whenever `D` is found append that value and decrement its count for next iteration.
* finally when the loop is finished before returning append either of `D/I` as they will be the same.

```python
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        inc,dec = 0, n
        perm = [0]*(n+1)

        for i in range(n):
            if s[i] == 'I':
                perm[i] = inc
                inc += 1
            else:
                perm[i] = dec
                dec -= 1 
        
        perm[n] = inc

        return perm
```
---------------------------------------------------------------------------------
## Optimal Solution
```python
def diStringMatch(s: str) -> List[int]:
        low , high = 0 , len(s)
        result = []

        for char in s:
            if char == "I":
                result.append(low)
                low +=1
            else:
                result.append(high)
                high -=1

        result.append(low)

        return result
```
