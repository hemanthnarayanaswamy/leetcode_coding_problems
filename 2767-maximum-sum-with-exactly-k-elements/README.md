<h2><a href="https://leetcode.com/problems/maximum-sum-with-exactly-k-elements">2767. Maximum Sum With Exactly K Elements </a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and an integer <code>k</code>. Your task is to perform the following operation <strong>exactly</strong> <code>k</code> times in order to maximize your score:</p>

<ol>
	<li>Select an element <code>m</code> from <code>nums</code>.</li>
	<li>Remove the selected element <code>m</code> from the array.</li>
	<li>Add a new element with a value of <code>m + 1</code> to the array.</li>
	<li>Increase your score by <code>m</code>.</li>
</ol>

<p>Return <em>the maximum score you can achieve after performing the operation exactly</em> <code>k</code> <em>times.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], k = 3
<strong>Output:</strong> 18
<strong>Explanation:</strong> We need to choose exactly 3 elements from nums to maximize the sum.
For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
So, we will return 18.
It can be proven, that 18 is the maximum answer that we can achieve.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,5,5], k = 2
<strong>Output:</strong> 11
<strong>Explanation:</strong> We need to choose exactly 2 elements from nums to maximize the sum.
For the first iteration, we choose 5. Then sum is 5 and nums = [5,5,6]
For the second iteration, we choose 6. Then sum is 5 + 6 = 11 and nums = [5,5,7]
So, we will return 11.
It can be proven, that 11 is the maximum answer that we can achieve.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<style type="text/css">.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; 
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
</style>

# Approach 
```ini
The sum of all integers from 1 to n inclusive is n(n + 1)/2.

The sum of all integers from m to n inclusive = (the sum from 1 to n inclusive) - (the sum from 1 to m - 1 inclusive)

= n(n + 1)/2 - m(m - 1)/2

Example: The sum of all the integers from 6 to 13 inclusive =

13 x 14/2 - 6 x 5/2 = 91 - 15 = 76

6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 = 76

If you meant exclusive, the sum of all integers from m to n exclusive = (the sum from 1 to n - 1 inclusive) - (the sum from 1 to m inclusive) = n(n - 1)/2 - m(m + 1)/2

Example: The sum of all the integers from 9 to 15 exclusive =

15 x 14/2 - 9 x 10/2 = 105 - 45 = 60

10 + 11 + 12 + 13 + 14 = 60
```

# Solution 
* First find the maximum number that is the array and add `k` to the max number and compute the sum between `max num and newly added number inclusive`

```ini 
max = 5
added_new = 5 + k = 5 + 2 = 7

sum = 5 + 6 + 7 

formula to compute = n(n+1) // 2 - m(m-1) // 2= 7(7+1)// 2 - 5(5-1)//2 = 28 - 10 = 18 
```
```python
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        chosen_num = max(nums)
        k_operation = chosen_num + k - 1

        maxSum = (k_operation*(k_operation + 1)) - (chosen_num*(chosen_num -1))
        return maxSum // 2
```

# OPtimal Solution 
```ini 
* Shortcut formula 

m = max(nums)
n = m + k - 1

result = (n -m +1)*(m+n)// 2
=(m+k-1-m+1)*(m+m+k-1)//2 
= k(2m+k-1)//2
```

```python
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
       z = 2*max(nums)-1+k
       return z * k //2
```

