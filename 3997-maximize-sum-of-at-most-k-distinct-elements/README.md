<h2><a href="https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements">3997. Maximize Sum of At Most K Distinct Elements</a></h2><h3>Easy</h3><hr><p>You are given a <strong>positive</strong> integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>Choose at most <code>k</code> elements from <code>nums</code> so that their sum is maximized. However, the chosen numbers must be <strong>distinct</strong>.</p>

<p>Return an array containing the chosen numbers in <strong>strictly descending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [84,93,100,77,90], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[100,93,90]</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum sum is 283, which is attained by choosing 93, 100 and 90. We rearrange them in strictly descending order as <code>[100, 93, 90]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [84,93,100,77,93], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[100,93,84]</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum sum is 277, which is attained by choosing 84, 93 and 100. We rearrange them in strictly descending order as <code>[100, 93, <span class="example-io">84</span>]</code>. We cannot choose 93, 100 and 93 because the chosen numbers must be distinct.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,2,2,2], k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum sum is 3, which is attained by choosing 1 and 2. We rearrange them in strictly descending order as <code>[2, 1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>

# Solution 
* Good Problem, We need to get the top k distinct elements from the given number array. 
* First we remove all the duplicates using the set, and sort the set in reverse order. 
* Give the sliced result till k. 

```python
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        distinctNums = sorted(set(nums), reverse=True)

        return distinctNums[:k]
```
