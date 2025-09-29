<h2><a href="https://leetcode.com/problems/flipping-an-image">861. Flipping an Image</a></h2><h3>Easy</h3><hr><p>Given an <code>n x n</code> binary matrix <code>image</code>, flip the image <strong>horizontally</strong>, then invert it, and return <em>the resulting image</em>.</p>

<p>To flip an image horizontally means that each row of the image is reversed.</p>

<ul>
	<li>For example, flipping <code>[1,1,0]</code> horizontally results in <code>[0,1,1]</code>.</li>
</ul>

<p>To invert an image means that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.</p>

<ul>
	<li>For example, inverting <code>[0,1,1]</code> results in <code>[1,0,0]</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> image = [[1,1,0],[1,0,1],[0,0,0]]
<strong>Output:</strong> [[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output:</strong> [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>images[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

# Solution 
```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        res = []

        for i in range(n):
            tmp = image[i][::-1]
            for j in range(n):
                if tmp[j]:
                    tmp[j] = 0
                else:
                    tmp[j] = 1
            res.append(tmp)
        
        return res
```
---
```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            # Reverse and invert simultaneously
            for i in range((n + 1) // 2):
                # Swap + invert
                row[i], row[n - 1 - i] = row[n - 1 - i] ^ 1, row[i] ^ 1
        return image
```
---
```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            i.reverse()
            res.append([x ^ 1 for x in i])
        return res
```
