<h2><a href="https://leetcode.com/problems/sum-of-variable-length-subarrays">3731. Sum of Variable Length Subarrays</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> of size <code>n</code>. For <strong>each</strong> index <code>i</code> where <code>0 &lt;= i &lt; n</code>, define a <span data-keyword="subarray-nonempty">subarray</span> <code>nums[start ... i]</code> where <code>start = max(0, i - nums[i])</code>.</p>

<p>Return the total sum of all elements from the subarray defined for each index in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>nums[0] = [2]</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>nums[0 ... 1] = [2, 3]</code></td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 2] = [3, 1]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><strong>Total Sum</strong></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">11</td>
		</tr>
	</tbody>
</table>

<p>The total sum is 11. Hence, 11 is the output.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>nums[0] = [3]</code></td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>nums[0 ... 1] = [3, 1]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 2] = [1, 1]</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 3] = [1, 1, 2]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><strong>Total Sum</strong></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">13</td>
		</tr>
	</tbody>
</table>

<p>The total sum is 13. Hence, 13 is the output.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

# Brute-Force Solution 
```python
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        
        for i, num in enumerate(nums):
            start = max(0, i - num)
            subarray_sum = sum(nums[start:i+1])
            res += subarray_sum
        
        return res
```
---
# Optimal Solution 
we use the `prefix sum` of nums to compute the sum of the range from some indices `nums[j]..nums[i]` where `j<i`. At each step we add the previous value in the array which names `nums[i]` equal to the sum of the array up to index `i`.

When we need to exclude a range, for example if we need the sum of `nums[j..i]` where `j = max(0, i - nums[i])`, then we subtract `nums[j - 1]` if `j>0`. If for every index `i` `nums[i] == sum(nums[..i])` then `sum(nums[j..i] == nums[i] - nums[j - 1]` if `j > 0` else 0). Note that if `j=0` then we want `sum(nums[..i])`.

```python
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre = [0]
        for i, c in enumerate(nums):
            pre.append(pre[-1] + c)
            
        ans = 0
        for i, c in enumerate(nums):
            start = max(0, i-c)
            ans += pre[i+1] - pre[start]
        
        return ans
```
# Solution 
* Here we are keeping track of change in new Start and based on the position on new start we either remove the elements sum or add element sum into the totalResult. 
```python
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        start = 0
        totalSum = 0

        for i, num in enumerate(nums):
            totalSum += num 

            newStart = max(0 , i - num)
            if newStart > start:
                totalSum -= sum(nums[start:newStart])
                start = newStart
            elif 0 <= newStart < start:
                totalSum += sum(nums[newStart:start])
                start = newStart
            
            res += totalSum
        
        return res
```
---
