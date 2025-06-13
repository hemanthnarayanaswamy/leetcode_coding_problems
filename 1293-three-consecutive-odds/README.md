<h2><a href="https://leetcode.com/problems/three-consecutive-odds">1293. Three Consecutive Odds</a></h2><h3>Easy</h3><hr>Given an integer array <code>arr</code>, return <code>true</code>&nbsp;if there are three consecutive odd numbers in the array. Otherwise, return&nbsp;<code>false</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,6,4,1]
<strong>Output:</strong> false
<b>Explanation:</b> There are no three consecutive odds.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,34,3,4,5,7,23,12]
<strong>Output:</strong> true
<b>Explanation:</b> [5,7,23] are three consecutive odds.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>

 # Solution 
 * We'll use two loops to reduce the complexity one to get the modulo values for even its zero and odd its one 
 * Next loop to do a sliding window to see if the sum is three for 3 consecutive odd numbers 

```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        arr = [num%2 for num in arr]

        for i in range(len(arr)-2):
            if sum(arr[i:i+3]) == 3:
                return True 
        
        return False
```
	
	
# 	Optimal Solution
```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        
        for num in arr:
            if num % 2:
                count+=1
                if count == 3:
                    return True
            else:
                count = 0

        return False
```
