<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">1468. Check If N and Its Double Exist</a></h2><h3>Easy</h3><hr><p>Given an array <code>arr</code> of integers, check if there exist two indices <code>i</code> and <code>j</code> such that :</p>

<ul>
	<li><code>i != j</code></li>
	<li><code>0 &lt;= i, j &lt; arr.length</code></li>
	<li><code>arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 500</code></li>
	<li><code>-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>

# Solution Approach
* It can be solved using the brute force approach 

```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Step 1: Iterate through all pairs of indices
        for i in range(len(arr)):
            for j in range(len(arr)):
                # Step 2: Check the conditions
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        # No valid pair found
        return False
```
------------
### My Solution
```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrFreq = Counter(arr)

        for key in arrFreq: 
            cond1, cond2, cond3 =  key * 2, key // 2, key % 2
            if cond1 == key or cond2 == key:
                if arrFreq[key] > 1:
                    return True
                else:
                    continue 

            if cond1 in arrFreq:
                return True
            
            if cond3 == 0 and cond2 in arrFreq:
                return True
        
        return False
```
---
### Improved Solution
```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = Counter(arr)

        for num in arr:
            # Check for double
            if num != 0 and 2 * num in count:
                return True
								
            # Handle zero case (ensure there are at least two zeros)
            if num == 0 and count[num] > 1:
                return True

        return False
```
----------
# Optimal LookUP 
```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            # Check if 2 * num or num / 2 exists in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        # No valid pair found
        return False
```
