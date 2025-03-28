<h2><a href="https://leetcode.com/problems/arithmetic-subarrays">1752. Arithmetic Subarrays</a></h2><h3>Medium</h3><hr><p>A sequence of numbers is called <strong>arithmetic</strong> if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence <code>s</code> is arithmetic if and only if <code>s[i+1] - s[i] == s[1] - s[0] </code>for all valid <code>i</code>.</p>

<p>For example, these are <strong>arithmetic</strong> sequences:</p>

<pre>
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>The following sequence is not <strong>arithmetic</strong>:</p>

<pre>
1, 1, 2, 5, 7</pre>

<p>You are given an array of <code>n</code> integers, <code>nums</code>, and two arrays of <code>m</code> integers each, <code>l</code> and <code>r</code>, representing the <code>m</code> range queries, where the <code>i<sup>th</sup></code> query is the range <code>[l[i], r[i]]</code>. All the arrays are <strong>0-indexed</strong>.</p>

<p>Return <em>a list of </em><code>boolean</code> <em>elements</em> <code>answer</code><em>, where</em> <code>answer[i]</code> <em>is</em> <code>true</code> <em>if the subarray</em> <code>nums[l[i]], nums[l[i]+1], ... , nums[r[i]]</code><em> can be <strong>rearranged</strong> to form an <strong>arithmetic</strong> sequence, and</em> <code>false</code> <em>otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = <code>[4,6,5,9,3,7]</code>, l = <code>[0,0,2]</code>, r = <code>[2,3,5]</code>
<strong>Output:</strong> <code>[true,false,true]</code>
<strong>Explanation:</strong>
In the 0<sup>th</sup> query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1<sup>st</sup> query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2<sup>nd</sup> query, the subarray is <code>[5,9,3,7]. This</code> can be rearranged as <code>[3,5,7,9]</code>, which is an arithmetic sequence.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
<strong>Output:</strong> [false,true,false,false,true,true]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == l.length</code></li>
	<li><code>m == r.length</code></li>
	<li><code>2 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= m &lt;= 500</code></li>
	<li><code>0 &lt;= l[i] &lt; r[i] &lt; n</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

## Solution Approach 

```python
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        answer = [True]*m    ## Define answer which should be equal to len m
        i = 0   ## Intiating a pointer to iterate through the sub arrays list in l, r

        while i < m:                                                                   # untill i reach last 
            sub_nums = sorted(nums[l[i]:r[i]+1])                        # Compute and Sort the Sub-array

            temp_diff = sub_nums[1] - sub_nums[0]                  # Reference Arthemetic Difference
            
            for x in range(1, len(sub_nums)-1):                           # Check if sub array is arthemic array or not
                if sub_nums[x+1] - sub_nums[x] != temp_diff:
                    answer[i] = False                                               # If not False and break
                    break
            i += 1                                                                       # Increment pointer to move to next sub array

        return answer
```

## Improved Solution

```python
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        is_arithmetic = []
        for i in range(len(l)):
            is_arithmetic.append(self.is_arithmetic_sequence(nums[l[i]: r[i] + 1]))

        return is_arithmetic



    def is_arithmetic_sequence(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False

        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
```
