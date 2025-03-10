<h2><a href="https://leetcode.com/problems/container-with-most-water">11. Container With Most Water</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" />
<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution Approach 
* The basic idea is to calculate the maximum area of a rectangle for the given heights.
* we initiate the left and right pointers, then calculate and store the results as we follow. 
* based on the height we either increment the left or the right pointer. 

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        l, r = 0, len(heights)-1 
        while l < r:
            result.append(min(heights[l], heights[r])*abs(r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max(result)
```
* Some Areas to improve is how we are storing the result, instead of using a list we can store only the maximum result 

```python 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1 
        while l < r:
            max_area = min(heights[l], heights[r])*abs(r-l)
            if result < max_area:
                result = max_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return result
```

## Optimal Solution 
* It can be further improved into one condition and calculation 
```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1 
        while l < r:
            if heights[l] < heights[r]:
                max_area = heights[l]*(r-l)
                l += 1
            else:
                max_area = heights[r]*(r-l)
                r -= 1
            if result < max_area:
                result = max_area
        
        return result
```

