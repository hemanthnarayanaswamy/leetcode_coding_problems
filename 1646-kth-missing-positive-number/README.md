<h2><a href="https://leetcode.com/problems/kth-missing-positive-number">1646. Kth Missing Positive Number</a></h2><h3>Easy</h3><hr><p>Given an array <code>arr</code> of positive integers sorted in a <strong>strictly increasing order</strong>, and an integer <code>k</code>.</p>

<p>Return <em>the</em> <code>k<sup>th</sup></code> <em><strong>positive</strong> integer that is <strong>missing</strong> from this array.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,3,4,7,11], k = 5
<strong>Output:</strong> 9
<strong>Explanation: </strong>The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup>&nbsp;missing positive integer is 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4], k = 2
<strong>Output:</strong> 6
<strong>Explanation: </strong>The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>arr[i] &lt; arr[j]</code> for <code>1 &lt;= i &lt; j &lt;= arr.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<p>Could you solve this problem in less than O(n) complexity?</p>

# Solution 
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        counter = 1
        res = []

        while len(res) < k:
            if  i < len(arr) and arr[i] == counter:
                i += 1
            else:
                res.append(counter)
            counter += 1
        
        return res[k-1]
```
---
# Improved Solution
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        counter = 1

        while k:
            if  i < len(arr) and arr[i] == counter:
                i += 1
            else:
                k -= 1

            counter += 1
        
        return counter - 1
```

--- 
# Optimal Solution 
```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nextNum = 1

        for num in arr:
            while num != nextNum:
                if k == 1:
                    return nextNum
                nextNum += 1
                k -= 1
            nextNum += 1
        
        return nextNum + k - 1
```

# Binary Search 
```ini
# At any index i:
missing_up_to_here = arr[i] - (i + 1)

 We're searching for the position where:
- missing_count < k (need to go right)
- missing_count >= k (found our boundary)
```

```ini
arr = [2, 3, 4, 7, 11], k = 5

# Missing counts at each position:
# arr[0] = 2: missing = 2 - 1 = 1
# arr[1] = 3: missing = 3 - 2 = 1  
# arr[2] = 4: missing = 4 - 3 = 1
# arr[3] = 7: missing = 7 - 4 = 3
# arr[4] = 11: missing = 11 - 5 = 6

# Binary search for k=5:
# We want position where missing >= 5
# Position 4 has 6 missing numbers >= 5
# So left = 4

# left = 4, so we look at arr[3] = 7
# missing_before_left = 7 - 4 = 3
# We need 5 missing numbers total
# Remaining needed = 5 - 3 = 2
# Answer = arr[3] + 2 = 7 + 2 = 9 ✓
```

```python
while left < right:
        mid = (left + right) // 2
        if arr[mid] - (mid + 1) < k:
            left = mid + 1
        else:
            right = mid
    
    # Correct calculation:
    if left == 0:
        return k
    else:
        return arr[left - 1] + k - (arr[left - 1] - left)
```

```python
class Solution:
    def findKthPositive(self, arr, k):
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2 
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid 
        return r + k
```
