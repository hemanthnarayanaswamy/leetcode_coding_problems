<h2><a href="https://leetcode.com/problems/count-complete-subarrays-in-an-array">2856. Count Complete Subarrays in an Array</a></h2><h3>Medium</h3><hr><p>You are given an array <code>nums</code> consisting of <strong>positive</strong> integers.</p>

<p>We call a subarray of an array <strong>complete</strong> if the following condition is satisfied:</p>

<ul>
	<li>The number of <strong>distinct</strong> elements in the subarray is equal to the number of distinct elements in the whole array.</li>
</ul>

<p>Return <em>the number of <strong>complete</strong> subarrays</em>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,5,5,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2000</code></li>
</ul>

## WRONG
* You are shrinking only `while freq[nums[left]] > 1`. That means you stop shrinking before testing all valid minimal windows. As a result, you under-count valid subarrays
```python
what is wrong with the solution
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        k = len(set(nums))
        left = 0
        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

            while len(freq) == k and freq[nums[left]] > 1:
                freq[nums[left]] -= 1
                left += 1
            
            if len(freq) == k:
                count += left + 1
        
        return count
```

* You must shrink the window while removing the left element does NOT break completeness.
```
Temporarily decrease the count
If the window is still complete → keep shrinking
Otherwise → stop shrinking and restore
```
```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        k = len(set(nums))
        left = 0
        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

            while len(freq) == k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    freq[nums[left]] += 1
                    break
                left += 1

            if len(freq) == k:
                count += left + 1

        return count
```
## Alternative Approach 
* If subarray `[left .. right]` is complete. then every longer subarray `[left .. right+1] [left .. right+2] [left .. right+3] ..` is also complete.
**Because once you already have all required elements, adding more elements can’t remove them.**

```ini
n = len(nums)
right = current right pointer index

There are (n - right) possible subarrays

that start at the same left index
and still include all required elements.
```

```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        k = len(set(nums))
        left = 0
        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

            while len(freq) == k:
                count += (n - i)
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count
```

```ini
left + 1   Number of valid start indices
n - right  Number of valid end indices
```
