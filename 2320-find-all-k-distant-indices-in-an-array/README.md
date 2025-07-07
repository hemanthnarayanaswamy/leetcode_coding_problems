<h2><a href="https://leetcode.com/problems/find-all-k-distant-indices-in-an-array">2320. Find All K-Distant Indices in an Array</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and two integers <code>key</code> and <code>k</code>. A <strong>k-distant index</strong> is an index <code>i</code> of <code>nums</code> for which there exists at least one index <code>j</code> such that <code>|i - j| &lt;= k</code> and <code>nums[j] == key</code>.</p>

<p>Return <em>a list of all k-distant indices sorted in <strong>increasing order</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,9,1,3,9,5], key = 9, k = 1
<strong>Output:</strong> [1,2,3,4,5,6]
<strong>Explanation:</strong> Here, <code>nums[2] == key</code> and <code>nums[5] == key.
- For index 0, |0 - 2| &gt; k and |0 - 5| &gt; k, so there is no j</code> where <code>|0 - j| &lt;= k</code> and <code>nums[j] == key. Thus, 0 is not a k-distant index.
- For index 1, |1 - 2| &lt;= k and nums[2] == key, so 1 is a k-distant index.
- For index 2, |2 - 2| &lt;= k and nums[2] == key, so 2 is a k-distant index.
- For index 3, |3 - 2| &lt;= k and nums[2] == key, so 3 is a k-distant index.
- For index 4, |4 - 5| &lt;= k and nums[5] == key, so 4 is a k-distant index.
- For index 5, |5 - 5| &lt;= k and nums[5] == key, so 5 is a k-distant index.
- For index 6, |6 - 5| &lt;= k and nums[5] == key, so 6 is a k-distant index.
</code>Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2], key = 2, k = 2
<strong>Output:</strong> [0,1,2,3,4]
<strong>Explanation:</strong> For all indices i in nums, there exists some index j such that |i - j| &lt;= k and nums[j] == key, so every index is a k-distant index. 
Hence, we return [0,1,2,3,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>key</code> is an integer from the array <code>nums</code>.</li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>

# Brute Force Solution 
* We can enumerate all index pairs (i,j) and determine whether nums[j]=key and ∣i−j∣≤k. At the same time, we use the array res to maintain all indices of the k nearest neighbors. If both conditions are satisfied, we add i to the array res.

* To ensure that res does not contain duplicate indices and is in ascending order, we can first enumerate i in ascending order, then enumerate j, and terminate the inner loop each time i is added to res, proceeding to the next i. 
* Finally, the array res will contain the indices of all the k nearest neighbors that meet the requirements, and we can return it as the answer.
```python
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        n = len(nums)
        # traverse number pairs
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break  # early termination to prevent duplicate addition
        return res
```

# Optimal Solution 
* Let's assume the length of the array nums is n. Then, for any index j that satisfies nums[j]=key, all indices within the closed interval `[max(0,j−k),min(n−1,j+k)]` are K-neighbor indices (the maximum and minimum functions are used here to ensure the indices are valid).

`[start, end] = [ max(0, j–k) ,  min(n–1, j+k) ]`

```ini 
If k = 1 and your key was at position 3, then positions 2, 3, and 4 are in that “window.” Here 2 is minimum and 4 is maximum

If k = 2, you’d include 1, 2, 3, 4, 5 (as long as you don’t fall off the ends of the list).
```

1. Left boundary: normally you’d go to position j − k.

* But if j − k is negative (say you’re near the very start), there is no “–3”th person.
* So you “clamp” that start to 0 instead.
* That’s exactly what max(0, j − k) does:
* If j − k is at least 0, use it;
* otherwise use 0.

2. Right boundary: normally you’d go to position j + k.

* But if j + k goes past n–1 (the last person), there is no person at index n or n+1.
* So you “clamp” that end to n–1.
* That’s what min(n − 1, j + k) does:
* If j + k is at most n–1, use it;
* otherwise use n–1.


```python
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                l = max(0, j - k)
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)
        return res
```
