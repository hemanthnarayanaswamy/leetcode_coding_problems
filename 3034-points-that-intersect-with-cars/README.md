<h2><a href="https://leetcode.com/problems/points-that-intersect-with-cars">3034. Points That Intersect With Cars</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> 2D integer array <code>nums</code> representing the coordinates of the cars parking on a number line. For any index <code>i</code>, <code>nums[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> where <code>start<sub>i</sub></code> is the starting point of the <code>i<sup>th</sup></code> car and <code>end<sub>i</sub></code> is the ending point of the <code>i<sup>th</sup></code> car.</p>

<p>Return <em>the number of integer points on the line that are covered with <strong>any part</strong> of a car.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [[3,6],[1,5],[4,7]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [[1,3],[5,8]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums[i].length == 2</code></li>
	<li><code><font face="monospace">1 &lt;= start<sub>i</sub>&nbsp;&lt;= end<sub>i</sub>&nbsp;&lt;= 100</font></code></li>
</ul>

# Brute Force Solution 
* For each `start, end` create a range and append numbers from that range into the set. 
* That set will have all the unique numbers and the result will be the lenght of that set. 

```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = set()

        for s, e in nums:
            for i in range(s,e+1):
                res.add(i)
        
        return len(res)
```
---
# Optimal Solution 
**Sort the array according to first element and then starting from the 0th index remove the overlapping parts and return the count of non-overlapping points.**
```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums = sorted(nums, key=lambda x: x[0])
        preEnd = 0
        points = 0

        for start, end in nums:
            if start <= preEnd:
                if end < preEnd:
                    continue
                else:
                    points += (end - preEnd)
                    preEnd = end
            else:
                points += (end - start + 1)
                preEnd = end
        
        return points
```
```python
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums = sorted(nums, key=lambda x: x[0])
        points = preEnd = 0

        for start, end in nums:
            if start <= preEnd:
                if end > preEnd:
                    points += (end - preEnd)
                else:
                    continue
            else:
                points += (end - start + 1)

            preEnd = end
        
        return points
```
