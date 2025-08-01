<h2><a href="https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color">3553. Check if Two Chessboard Squares Have the Same Color</a></h2><h3>Easy</h3><hr><p>You are given two strings, <code>coordinate1</code> and <code>coordinate2</code>, representing the coordinates of a square on an <code>8 x 8</code> chessboard.</p>

<p>Below is the chessboard for reference.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/17/screenshot-2021-02-20-at-22159-pm.png" style="width: 400px; height: 396px;" /></p>

<p>Return <code>true</code> if these two squares have the same color and <code>false</code> otherwise.</p>

<p>The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coordinate1 = &quot;a1&quot;, coordinate2 = &quot;c3&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Both squares are black.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coordinate1 = &quot;a1&quot;, coordinate2 = &quot;h3&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>Square <code>&quot;a1&quot;</code> is black and <code>&quot;h3&quot;</code> is white.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>coordinate1.length == coordinate2.length == 2</code></li>
	<li><code>&#39;a&#39; &lt;= coordinate1[0], coordinate2[0] &lt;= &#39;h&#39;</code></li>
	<li><code>&#39;1&#39; &lt;= coordinate1[1], coordinate2[1] &lt;= &#39;8&#39;</code></li>
</ul>

# Solution 
* The logic is to {a:1, b:2, c:3, d:4, e:5, f:6, g:7, h:8} if the alphabet value and the number value are both `even-even or odd-odd` then the colour is the same 
* The color of the chessboard is black the sum of row coordinates and column coordinates is even. Otherwise, it's white.

```python
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return ((int(ord(coordinate1[0]) - 96) + int(coordinate1[1])) % 2) == ((int(ord(coordinate2[0]) - 96) + int(coordinate2[1])) % 2)
```

```python
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        return (alphabet[coordinate1[0]] + int(coordinate1[1])) % 2 == (alphabet[coordinate2[0]] + int(coordinate2[1])) % 2
```

```python
class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        one = ord(c1[0]) + int(c1[1])
        two = ord(c2[0]) + int(c2[1])
        return one % 2 == two % 2
```
