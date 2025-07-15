<h2><a href="https://leetcode.com/problems/min-max-game">2386. Min Max Game</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> whose length is a power of <code>2</code>.</p>

<p>Apply the following algorithm on <code>nums</code>:</p>

<ol>
	<li>Let <code>n</code> be the length of <code>nums</code>. If <code>n == 1</code>, <strong>end</strong> the process. Otherwise, <strong>create</strong> a new <strong>0-indexed</strong> integer array <code>newNums</code> of length <code>n / 2</code>.</li>
	<li>For every <strong>even</strong> index <code>i</code> where <code>0 &lt;= i &lt; n / 2</code>, <strong>assign</strong> the value of <code>newNums[i]</code> as <code>min(nums[2 * i], nums[2 * i + 1])</code>.</li>
	<li>For every <strong>odd</strong> index <code>i</code> where <code>0 &lt;= i &lt; n / 2</code>, <strong>assign</strong> the value of <code>newNums[i]</code> as <code>max(nums[2 * i], nums[2 * i + 1])</code>.</li>
	<li><strong>Replace</strong> the array <code>nums</code> with <code>newNums</code>.</li>
	<li><strong>Repeat</strong> the entire process starting from step 1.</li>
</ol>

<p>Return <em>the last number that remains in </em><code>nums</code><em> after applying the algorithm.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/04/13/example1drawio-1.png" style="width: 500px; height: 240px;" />
<pre>
<strong>Input:</strong> nums = [1,3,5,2,4,8,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 is already the last remaining number, so we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1024</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums.length</code> is a power of <code>2</code>.</li>
</ul>

# Solution 
* Need to simulate the description details as it is. 

```python
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        m = n // 2  # new array size
        newNum = nums

        while m:
            temp = [0]*m 

            for i in range(m):
                if i % 2: # construct the new temp array with the even or odd conditions
                    temp[i] = max(newNum[2*i], newNum[2*i + 1])
                else:
                    temp[i] = min(newNum[2*i], newNum[2*i + 1])
            
            newNum = temp # assign temp to newNum array 
            m //= 2 # reduce the m
        
        return newNum[0]
```

# Optimal Solution 
```python
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            newNums = []
            count = 0
            for i in range(0, len(nums), 2):
                if count % 2 == 0:
                    newNums.append(min(nums[i], nums[i + 1]))
                else:
                    newNums.append(max(nums[i], nums[i + 1]))
                count += 1
            nums = newNums
            
        return nums[0]
```

```python
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            # pair up (nums[0],nums[1]), (nums[2],nums[3]), …
            pairs = zip(nums[::2], nums[1::2])
            # for each pair, take min if i is even, max if i is odd
            nums = [
                (a if a < b else b) if i % 2 == 0 else (a if a > b else b)
                for i, (a, b) in enumerate(pairs)
            ]
        return nums[0]
```
