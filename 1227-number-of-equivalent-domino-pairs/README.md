<h2><a href="https://leetcode.com/problems/number-of-equivalent-domino-pairs">1227. Number of Equivalent Domino Pairs</a></h2><h3>Easy</h3><hr><p>Given a list of <code>dominoes</code>, <code>dominoes[i] = [a, b]</code> is <strong>equivalent to</strong> <code>dominoes[j] = [c, d]</code> if and only if either (<code>a == c</code> and <code>b == d</code>), or (<code>a == d</code> and <code>b == c</code>) - that is, one domino can be rotated to be equal to another domino.</p>

<p>Return <em>the number of pairs </em><code>(i, j)</code><em> for which </em><code>0 &lt;= i &lt; j &lt; dominoes.length</code><em>, and </em><code>dominoes[i]</code><em> is <strong>equivalent to</strong> </em><code>dominoes[j]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dominoes = [[1,2],[2,1],[3,4],[5,6]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= dominoes.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>dominoes[i].length == 2</code></li>
	<li><code>1 &lt;= dominoes[i][j] &lt;= 9</code></li>
</ul>

# Solution 
* We need to count all equivalent dominoes, where dominoes are represented by a pairs.
* Noticing that the elements in the pairs are all not greater than 9, we can concatenate each binary pair into a two-digit positive integer, i.e., (x,y)→10x+y. In this way, there is no need to use a hash table to count the number of elements, but we can directly use an array of length 100.

```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        result = 0

        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            
            result += num[val]
            num[val] += 1
        
        return result
```
