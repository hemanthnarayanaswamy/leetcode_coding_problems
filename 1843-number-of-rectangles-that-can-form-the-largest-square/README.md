<h2><a href="https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square">1843. Number Of Rectangles That Can Form The Largest Square</a></h2><h3>Easy</h3><hr><p>You are given an array <code>rectangles</code> where <code>rectangles[i] = [l<sub>i</sub>, w<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> rectangle of length <code>l<sub>i</sub></code> and width <code>w<sub>i</sub></code>.</p>

<p>You can cut the <code>i<sup>th</sup></code> rectangle to form a square with a side length of <code>k</code> if both <code>k &lt;= l<sub>i</sub></code> and <code>k &lt;= w<sub>i</sub></code>. For example, if you have a rectangle <code>[4,6]</code>, you can cut it to get a square with a side length of at most <code>4</code>.</p>

<p>Let <code>maxLen</code> be the side length of the <strong>largest</strong> square you can obtain from any of the given rectangles.</p>

<p>Return <em>the <strong>number</strong> of rectangles that can make a square with a side length of </em><code>maxLen</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> rectangles = [[5,8],[3,9],[5,12],[16,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> rectangles = [[2,3],[3,7],[4,3],[3,7]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 1000</code></li>
	<li><code>rectangles[i].length == 2</code></li>
	<li><code>1 &lt;= l<sub>i</sub>, w<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>l<sub>i</sub> != w<sub>i</sub></code></li>
</ul>

# Solution 
* First we need to find the maxLen of the square that can be formed out of all the rectangles. 
* While also keeping track of how many rectangles are forming the square of side x using hashMap 

```python
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squareSides = {}
        maxLen = 0

        for l, w in rectangles:
            s = min(l, w)
            squareSides[s] = squareSides.get(s, 0) + 1

            if s > maxLen:
                maxLen = s

        return squareSides[maxLen]
```

# Optimal Solution 
* Have counter instead of a HashMap. 

```python
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        count = 0

        for l, w in rectangles:
            side_len = l if l > w else w

            if side_len > max_len:
                max_len = side_len
                count = 1
            elif side_len == max_len:
                count += 1

        return count
```
				
