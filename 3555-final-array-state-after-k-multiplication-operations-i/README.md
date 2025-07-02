<h2><a href="https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/?envType=problem-list-v2&envId=n9iuhemc">3555. Final Array State After K Multiplication Operations I</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>, an integer <code>k</code>, and an integer <code>multiplier</code>.</p>

<p>You need to perform <code>k</code> operations on <code>nums</code>. In each operation:</p>

<ul>
	<li>Find the <strong>minimum</strong> value <code>x</code> in <code>nums</code>. If there are multiple occurrences of the minimum value, select the one that appears <strong>first</strong>.</li>
	<li>Replace the selected minimum value <code>x</code> with <code>x * multiplier</code>.</li>
</ul>

<p>Return an integer array denoting the <em>final state</em> of <code>nums</code> after performing all <code>k</code> operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3,5,6], k = 5, multiplier = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[8,4,6,5,6]</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[2, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[4, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 3</td>
			<td>[4, 4, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 4</td>
			<td>[4, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>After operation 5</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2], k = 3, multiplier = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">[16,8]</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Operation</th>
			<th>Result</th>
		</tr>
		<tr>
			<td>After operation 1</td>
			<td>[4, 2]</td>
		</tr>
		<tr>
			<td>After operation 2</td>
			<td>[4, 8]</td>
		</tr>
		<tr>
			<td>After operation 3</td>
			<td>[16, 8]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>1 &lt;= multiplier &lt;= 5</code></li>
</ul>

# Solution 
* You need to exactly simulate the process for k number of times using the while loop. 
* Find the minimum Number before the iteration and in the for loop find the number and do the multiplication and reduce the k value for number of operation perfomed

```python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            minNum = min(nums)
            for i in range(len(nums)):
                if nums[i] == minNum:
                    nums[i] *= multiplier
                    break
            k -= 1
        
        return nums
```

# Improved Solution 
* Need to use the Heap Queue instead of computing the minimum for each and every iteration 
```python
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for _ in range(k):
            # find the index of the minimum element
            min_idx = 0
            for i in range(1, n):
                if nums[i] < nums[min_idx]:
                    min_idx = i
            # multiply that minimum
            nums[min_idx] *= multiplier
        return nums
```
