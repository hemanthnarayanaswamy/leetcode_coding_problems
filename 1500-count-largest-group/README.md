<h2><a href="https://leetcode.com/problems/count-largest-group">1500. Count Largest Group</a></h2><h3>Easy</h3><hr><p>You are given an integer <code>n</code>.</p>

<p>We need to group the numbers from <code>1</code> to <code>n</code> according to the sum of its digits. For example, the numbers 14 and 5 belong to the <strong>same</strong> group, whereas 13 and 3 belong to <strong>different</strong> groups.</p>

<p>Return the number of groups that have the largest size, i.e. the <strong>maximum</strong> number of elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 groups [1], [2] of size 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


# Solution 
```ini 
But the problem only needs a one-time digit sum, not the final single-digit result.

Example:
	•	For n = 13, 1 + 3 = 4 — this is what we need.
	•	But your function will do:
	•	1 + 3 = 4 → return 4 ✅ (fine here)
	
	•	For n = 99:
	•	9 + 9 = 18, loop again: 1 + 8 = 9 → returns 9 ❌
	•	But we want to group 99 under 18, not 9.
```

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        numGroup = {}
        maxGroupSize = 0
        count = 0

        for i in range(1, n+1):
            temp = sum([int(j) for j in str(i)])
            numGroup[temp] = numGroup.get(temp, 0) + 1

        for v in numGroup.values():
            if v > maxGroupSize:
                maxGroupSize = v
                count = 0

            if v == maxGroupSize:
                count += 1
        
        return count
```
# Improved Solution 
```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        numGroup = {}

        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        for i in range(1, n+1):
            temp = digit_sum(i)
            numGroup[temp] = numGroup.get(temp, 0) + 1
        
        maxSize = max(numGroup.values())
        return sum(1 for v in numGroup.values() if v == maxSize)
```

# Wrong Solution 
```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        numGroup = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        count = 0

        def numHelper(n):
            result = 0
            while n:
                result += n % 10 
                n = n // 10 
                if n == 0 and result >= 10:
                    n = result 
                    result = 0
                elif n == 0 and result <= 9:
                    return result 


        for i in range(1, n+1):
            if i < 9:
                numGroup[i] = numGroup.get(i, 0) + 1
            else:
                temp = numHelper(i)
                numGroup[temp] = numGroup.get(temp, 0) + 1
        
        maxGroupSize = 0
        print(numGroup)

        for v in numGroup.values():
            if v > maxGroupSize:
                maxGroupSize = v
                count = 0

            if v == maxGroupSize:
                count += 1
        
        return count
```
