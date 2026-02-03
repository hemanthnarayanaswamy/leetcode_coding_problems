<h2><a href="https://leetcode.com/problems/prime-in-diagonal">2722. Prime In Diagonal</a></h2><h3>Easy</h3><hr><p>You are given a 0-indexed two-dimensional integer array <code>nums</code>.</p>

<p>Return <em>the largest <strong>prime</strong> number that lies on at least one of the <b>diagonals</b> of </em><code>nums</code>. In case, no prime is present on any of the diagonals, return<em> 0.</em></p>

<p>Note that:</p>

<ul>
	<li>An integer is <strong>prime</strong> if it is greater than <code>1</code> and has no positive integer divisors other than <code>1</code> and itself.</li>
	<li>An integer <code>val</code> is on one of the <strong>diagonals</strong> of <code>nums</code> if there exists an integer <code>i</code> for which <code>nums[i][i] = val</code> or an <code>i</code> for which <code>nums[i][nums.length - i - 1] = val</code>.</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png" style="width: 181px; height: 121px;" /></p>

<p>In the above diagram, one diagonal is <strong>[1,5,9]</strong> and another diagonal is<strong> [3,5,7]</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [[1,2,3],[5,6,7],[9,10,11]]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [[1,2,3],[5,17,7],[9,11,10]]
<strong>Output:</strong> 17
<strong>Explanation:</strong> The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 300</code></li>
	<li><code>nums.length == nums<sub>i</sub>.length</code></li>
	<li><code>1 &lt;= nums<span style="font-size: 10.8333px;">[i][j]</span>&nbsp;&lt;= 4*10<sup>6</sup></code></li>
</ul>

# Solution 
1. **Primary diagonal:** Elements where `row index = column index`.
2. **Secondary diagonal:** Elements where `row index + column index = number of columns - 1`.

### Check if the number is Prime
```python
def isPrime(num):
    if num<= 1:
        return False
    for i in range(2, int(num**0.5)+1): # for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
```
---
```python
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
		
        def isPrime(num):
            if num<= 1:
                return False
            for i in range(2, int(num**0.5)+1): # for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True
        
        res = 0
        n = len(nums[0])
        m = len(nums)

        for i in range(m):
            for j in range(n):
                if i == j or i + j == n - 1:
                    num = nums[i][j]
                    if num > res and isPrime(num):
                        res = num
        
        return res
```
---
```ini
For primary Diagnol we know i == j, that means nums[i][j] can be written as nums[i][i] or nums[j][j]
For the Secondary Diagnol, 

i + j = n - 1
j = n - i - 1
so nums[i][j] can be written as nums[i][n -1 - i]

This means we don't need to a variable j and we can avoid using the seconday for loop
```

```python
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num<= 1:
                return False
            for i in range(2, int(num**0.5)+1): # for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return 0
            return num
        
        res = 0
        n = len(nums)

        for i in range(n):
            num1 = nums[i][i]
            num2 = nums[i][n - i - 1]
            res = max(res, isPrime(num1), isPrime(num2))
        
        return res
```
---
```python
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num<= 1:
                return False
            for i in range(2, int(num**0.5)+1): # for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True
        
        res = 0
        n = len(nums)

        for i in range(n):
            num1 = nums[i][i]
            num2 = nums[i][n - i - 1]
            
            if num1 > res and isPrime(num1):
                res = num1
            
            if num2 > res and isPrime(num2):
                res = num2
        
        return res
```
