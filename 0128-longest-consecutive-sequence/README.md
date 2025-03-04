<h2><a href="https://leetcode.com/problems/longest-consecutive-sequence">128. Longest Consecutive Sequence</a></h2><h3>Medium</h3><hr><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,2]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## Solution Approach 
* We can solve by removeing the duplicated by using sets and than sorting the array.
* Than Iterate throught the array by keeping track of the max_lenght

```python
if not nums:
            return 0
            
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        max_consecutive = 1
        curr_consecutive = 1
        for i in range(1, n):
            if nums[i-1] + 1 == nums[i]:
                curr_consecutive += 1
            else:
                max_consecutive = max(max_consecutive, curr_consecutive)
                curr_consecutive = 1

        max_consecutive = max(max_consecutive, curr_consecutive)

        return max_consecutive
```

## Solution Approach without Sorting 
* We remove the Duplicate elements by using the set. 
* We iterrate throught to set by checking if `num-1` is not present, because if that `num-1` is not present in the set that means it is the starting point. 
* After determining the starting point we set `current = num`, `lenght = 1`
* Than we run a internal `while` Loop with condition `if current + 1 in nums` 
* Than update the `current and lenght` 
* Max_longest = max(max_longest, lenth)

```python 
def longestconsecutive(nums):
    nums = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest
```



