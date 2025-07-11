<h2><a href="https://leetcode.com/problems/two-furthest-houses-with-different-colors">2199. Two Furthest Houses With Different Colors</a></h2><h3>Easy</h3><hr><p>There are <code>n</code> houses evenly lined up on the street, and each house is beautifully painted. You are given a <strong>0-indexed</strong> integer array <code>colors</code> of length <code>n</code>, where <code>colors[i]</code> represents the color of the <code>i<sup>th</sup></code> house.</p>

<p>Return <em>the <strong>maximum</strong> distance between <strong>two</strong> houses with <strong>different</strong> colors</em>.</p>

<p>The distance between the <code>i<sup>th</sup></code> and <code>j<sup>th</sup></code> houses is <code>abs(i - j)</code>, where <code>abs(x)</code> is the <strong>absolute value</strong> of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg1.png" style="width: 610px; height: 84px;" />
<pre>
<strong>Input:</strong> colors = [<u><strong>1</strong></u>,1,1,<strong><u>6</u></strong>,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg2.png" style="width: 426px; height: 84px;" />
<pre>
<strong>Input:</strong> colors = [<u><strong>1</strong></u>,8,3,8,<u><strong>3</strong></u>]
<strong>Output:</strong> 4
<strong>Explanation:</strong> In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> colors = [<u><strong>0</strong></u>,<strong><u>1</u></strong>]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n ==&nbsp;colors.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= colors[i] &lt;= 100</code></li>
	<li>Test data are generated such that <strong>at least</strong> two houses have different colors.</li>
</ul>

# Wrong Solution 
* Lets create a Map for the different colours and it highest index in the map. 
* The maximum distance between them will be the difference between the min and max index in the hash map. 

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        housePos = {}

        for i, c in enumerate(colors):
            housePos[c] = max(housePos.get(c, 0), i)

        house1 = min(housePos.values())
        house2 = max(housePos.values())

        return house2 - house1
```
* The issue with this approach is it fails some edge cases `[9,9,9,18,9,9,9,9,9,18]` answer should be 9 but our case it is 1
* We are sorting only the max value of i for the house so it'll fail for the above case. 

# Solution 
* Lets use `Two POINTER` and two different iterations.
1. In the first iteration we keep the left pointer same and keep moving the right until we find house with different colours and store the result from it and break the loop.
2. In the second iteration we do the same  as above but now we keep the right pointer same and move the left pointer, till we encounter different houses, store result and break the Loop.
3. Return the maximum of the results stored. 

`The maximum distance will come from either the pair of the leftmost house and some house on the right with a different color`
`or` `The pair of the rightmost house and possibly some house on the left with a different color.`

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        h1, h2 = 0, len(colors)-1

        res = []

        while h1 < h2:
            if colors[h1] != colors[h2]:
                res.append(h2 - h1)
                break
            else:
                h2 -= 1

        h2 = len(colors)-1

        while h1 < h2:
            if colors[h1] != colors[h2]:
                res.append(h2 - h1)
                break
            else:
                h1 += 1
        
        return max(res)
````

# Optimal Solutions 
```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=colors[0]:
                diff = i
                ans = max(ans,diff)
        for i in range(len(colors)):
            if colors[i]!=colors[len(colors)-1]:
                diff = len(colors)-1-i
                ans = max(ans,diff)
        return ans
```
