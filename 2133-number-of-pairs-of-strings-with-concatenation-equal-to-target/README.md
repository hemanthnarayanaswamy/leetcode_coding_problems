<h2><a href="https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target">2133. Number of Pairs of Strings With Concatenation Equal to Target</a></h2><h3>Medium</h3><hr><p>Given an array of <strong>digit</strong> strings <code>nums</code> and a <strong>digit</strong> string <code>target</code>, return <em>the number of pairs of indices </em><code>(i, j)</code><em> (where </em><code>i != j</code><em>) such that the <strong>concatenation</strong> of </em><code>nums[i] + nums[j]</code><em> equals </em><code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;777&quot;,&quot;7&quot;,&quot;77&quot;,&quot;77&quot;], target = &quot;7777&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> Valid pairs are:
- (0, 1): &quot;777&quot; + &quot;7&quot;
- (1, 0): &quot;7&quot; + &quot;777&quot;
- (2, 3): &quot;77&quot; + &quot;77&quot;
- (3, 2): &quot;77&quot; + &quot;77&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;123&quot;,&quot;4&quot;,&quot;12&quot;,&quot;34&quot;], target = &quot;1234&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Valid pairs are:
- (0, 1): &quot;123&quot; + &quot;4&quot;
- (2, 3): &quot;12&quot; + &quot;34&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;], target = &quot;11&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> Valid pairs are:
- (0, 1): &quot;1&quot; + &quot;1&quot;
- (1, 0): &quot;1&quot; + &quot;1&quot;
- (0, 2): &quot;1&quot; + &quot;1&quot;
- (2, 0): &quot;1&quot; + &quot;1&quot;
- (1, 2): &quot;1&quot; + &quot;1&quot;
- (2, 1): &quot;1&quot; + &quot;1&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 100</code></li>
	<li><code>2 &lt;= target.length &lt;= 100</code></li>
	<li><code>nums[i]</code> and <code>target</code> consist of digits.</li>
	<li><code>nums[i]</code> and <code>target</code> do not have leading zeros.</li>
</ul>

# Notes
"""
PROBLEM: Given array of strings and target, count pairs where nums[i] + nums[j] == target (i ≠ j)

KEY INSIGHTS:
1. If nums[i] + nums[j] == target, then:
   - nums[i] = prefix of target
   - nums[j] = suffix of target
   - len(prefix) + len(suffix) = len(target)

2. Use frequency counter to avoid O(n²) nested loops

ALGORITHM:
1. Count frequency of all strings
2. For each unique string that's a valid prefix:
   - Find required suffix = target[len(prefix):]
   - If suffix exists in frequency map:
     - If prefix ≠ suffix: count += freq[prefix] × freq[suffix]
     - If prefix = suffix: count += freq[prefix] × (freq[prefix] - 1)

EDGE CASE: When prefix == suffix
- Can't use same index twice
- Use permutation formula: n × (n-1)

TIME: O(n × m) where n = len(nums), m = avg string length
SPACE: O(n)
"""
# Brute Force Solution 
* Brute Force solution is easy.

```python
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        
        return count 
```

# Improved Solution 
```python
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        nums_freq = Counter(nums)  # Python convention: snake_case
        count = 0
        target_len = len(target)   # Cache target length

        for prefix in set(nums):
            prefix_len = len(prefix)
            if prefix_len >= target_len:
                continue

            if target.startswith(prefix):
                suffix = target[prefix_len:]

                if suffix in nums_freq:
                    suffix_count = nums_freq[suffix]
                    prefix_count = nums_freq[prefix]

                    if prefix != suffix:
                        count += suffix_count * prefix_count
                    else: 
                        count += prefix_count * (prefix_count - 1)
                    
        return count
```

# Optimal Solution 
```python
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        ans = 0 
        for k, v in freq.items(): 
            if target.startswith(k): 
                suffix = target[len(k):]
                ans += v * freq[suffix]
                if k == suffix: 
                    ans -= freq[suffix]
        return ans 
```


