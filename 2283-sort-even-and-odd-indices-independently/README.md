<h2><a href="https://leetcode.com/problems/sort-even-and-odd-indices-independently">2283. Sort Even and Odd Indices Independently</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. Rearrange the values of <code>nums</code> according to the following rules:</p>

<ol>
	<li>Sort the values at <strong>odd indices</strong> of <code>nums</code> in <strong>non-increasing</strong> order.

	<ul>
		<li>For example, if <code>nums = [4,<strong><u>1</u></strong>,2,<u><strong>3</strong></u>]</code> before this step, it becomes <code>[4,<u><strong>3</strong></u>,2,<strong><u>1</u></strong>]</code> after. The values at odd indices <code>1</code> and <code>3</code> are sorted in non-increasing order.</li>
	</ul>
	</li>
	<li>Sort the values at <strong>even indices</strong> of <code>nums</code> in <strong>non-decreasing</strong> order.
	<ul>
		<li>For example, if <code>nums = [<u><strong>4</strong></u>,1,<u><strong>2</strong></u>,3]</code> before this step, it becomes <code>[<u><strong>2</strong></u>,1,<u><strong>4</strong></u>,3]</code> after. The values at even indices <code>0</code> and <code>2</code> are sorted in non-decreasing order.</li>
	</ul>
	</li>
</ol>

<p>Return <em>the array formed after rearranging the values of</em> <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,1,2,3]
<strong>Output:</strong> [2,3,4,1]
<strong>Explanation:</strong> 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,<strong><u>1</u></strong>,2,<strong><u>3</u></strong>] to [4,<u><strong>3</strong></u>,2,<strong><u>1</u></strong>].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [<u><strong>4</strong></u>,1,<strong><u>2</u></strong>,3] to [<u><strong>2</strong></u>,3,<u><strong>4</strong></u>,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1]
<strong>Output:</strong> [2,1]
<strong>Explanation:</strong> 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
* Seperate the odd, even numbers index into different arrays and sort them based on condition ascending and descending. 
```python
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddSort = []
        evenSort = []
        result = []

        for i in range(len(nums)):
            if i % 2:
                oddSort.append(nums[i])
            else:
                evenSort.append(nums[i])
        
        oddSort.sort(reverse=True)
        evenSort.sort()

        for i in range(len(oddSort)):
            result.append(evenSort[i])
            result.append(oddSort[i])
        
        if len(result) == len(nums):
            return result 
        else:
            result.append(evenSort[-1])

        return result
```

# Optimal Solution
```python
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Extract even-indexed and odd-indexed elements
        evens = sorted(nums[::2])                      # ascending
        odds  = sorted(nums[1::2], reverse=True)       # descending

        # Allocate result array of the same length
        res = [None] * len(nums)
        # Place sorted values back into even and odd positions
        res[::2] = evens
        res[1::2] = odds

        return res
```
