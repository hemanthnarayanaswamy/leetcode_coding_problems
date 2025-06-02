<h2><a href="https://leetcode.com/problems/determine-color-of-a-chessboard-square">1920. Determine Color of a Chessboard Square</a></h2><h3>Easy</h3><hr><p>You are given <code>coordinates</code>, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png" style="width: 400px; height: 396px;" /></p>

<p>Return <code>true</code><em> if the square is white, and </em><code>false</code><em> if the square is black</em>.</p>

<p>The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> coordinates = &quot;a1&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> From the chessboard above, the square with coordinates &quot;a1&quot; is black, so return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> coordinates = &quot;h3&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> From the chessboard above, the square with coordinates &quot;h3&quot; is white, so return true.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> coordinates = &quot;c7&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>coordinates.length == 2</code></li>
	<li><code>&#39;a&#39; &lt;= coordinates[0] &lt;= &#39;h&#39;</code></li>
	<li><code>&#39;1&#39; &lt;= coordinates[1] &lt;= &#39;8&#39;</code></li>
</ul>

# Solution 
* If you observer the cheese patterns then the odd-odd and even-even row columns maps to black colour thats the hint 
* we are also converting the characters into numbers by `96 - ord(a) --> 96 -97 = 1` logic
* and check if the numbers are odd or even.

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - 96) % 2 == int(coordinates[1]) % 2:
            return False 
        else:
            return True
```

# Improved Solution
* Use the conditional checking to return automatically. 

```python 
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return not (ord(coordinates[0]) - 96) % 2 == int(coordinates[1]) % 2
```
