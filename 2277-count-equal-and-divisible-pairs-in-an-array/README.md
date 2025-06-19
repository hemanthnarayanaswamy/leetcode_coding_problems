<h2><a href="https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array">2277. Count Equal and Divisible Pairs in an Array</a></h2><h3>Easy</h3><hr>Given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>, return <em>the <strong>number of pairs</strong></em> <code>(i, j)</code> <em>where</em> <code>0 &lt;= i &lt; j &lt; n</code>, <em>such that</em> <code>nums[i] == nums[j]</code> <em>and</em> <code>(i * j)</code> <em>is divisible by</em> <code>k</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,2,2,2,1,3], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong>
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4], k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 100</code></li>
</ul>

# Brute Force 
* Two for loops check each number and don't forget the condition `(i, j) where 0 <= i < j < n` `j >i`.

```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j]:
                    if i*j % k == 0:
                        count += 1
        
        return count 
```

# Optimal Solution 
```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        group=defaultdict(list)
        c=0
        for i,num in enumerate(nums):
            if num in group:
                for j in group[num]:
                    if (j*i)%k==0:
                        c+=1
            group[num].append(i)
        return c
```

* Same approach as above with simpler syntax 

```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq=[[] for i in range(101)]
        cnt=0
        for j, x in enumerate(nums):
            for i in freq[x]:
                cnt+=(i*j%k==0)
            freq[x].append(j)
        return cnt
```
