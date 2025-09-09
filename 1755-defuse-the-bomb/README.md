<h2><a href="https://leetcode.com/problems/defuse-the-bomb">1755. Defuse the Bomb</a></h2><h3>Easy</h3><hr><p>You have a bomb to defuse, and your time is running out! Your informer will provide you with a <strong>circular</strong> array <code>code</code>&nbsp;of length of <code>n</code>&nbsp;and a key <code>k</code>.</p>

<p>To decrypt the code, you must replace every number. All the numbers are replaced <strong>simultaneously</strong>.</p>

<ul>
	<li>If <code>k &gt; 0</code>, replace the <code>i<sup>th</sup></code> number with the sum of the <strong>next</strong> <code>k</code> numbers.</li>
	<li>If <code>k &lt; 0</code>, replace the <code>i<sup>th</sup></code> number with the sum of the <strong>previous</strong> <code>k</code> numbers.</li>
	<li>If <code>k == 0</code>, replace the <code>i<sup>th</sup></code> number with <code>0</code>.</li>
</ul>

<p>As <code>code</code> is circular, the next element of <code>code[n-1]</code> is <code>code[0]</code>, and the previous element of <code>code[0]</code> is <code>code[n-1]</code>.</p>

<p>Given the <strong>circular</strong> array <code>code</code> and an integer key <code>k</code>, return <em>the decrypted code to defuse the bomb</em>!</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> code = [5,7,1,4], k = 3
<strong>Output:</strong> [12,10,16,13]
<strong>Explanation:</strong> Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> code = [1,2,3,4], k = 0
<strong>Output:</strong> [0,0,0,0]
<strong>Explanation:</strong> When k is zero, the numbers are replaced by 0. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> code = [2,4,9,3], k = -2
<strong>Output:</strong> [12,5,6,13]
<strong>Explanation:</strong> The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the <strong>previous</strong> numbers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == code.length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= code[i] &lt;= 100</code></li>
	<li><code>-(n - 1) &lt;= k &lt;= n - 1</code></li>
</ul>

# My Solution 
* Using the sliding Window approach, We first calculate the inital sum of window size `k`.
* Now as we move the window we remove the current element from the sum and add the next `i+k` element into the sum. This case is for k > 0. 
* We can follow the same approach for k < 0, we only need to reverse the given array and the result after the computation. 

```python
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * len(code)

        if k > 0:
            initialSum = sum(code[:k])
            for i in range(n):
                res[i] = initialSum - code[i] + code[(i+k) % n]
                initialSum = res[i]
        elif k < 0:
            k = -k
            code = code[::-1]
            initialSum = sum(code[:k])
            for i in range(n):
                res[i] = initialSum - code[i] + code[(i+k) % n]
                initialSum = res[i]
            
            res = res[::-1]
        
        return res
```
---
# Optimal Solution 
```python
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        if k == 0:
            return res 
        
        if k > 0:
            window_sum = sum(code[1:k+1])
        else:
            window_sum = sum(code[k:])
        
        res[0] = window_sum 

        for i in range(1, n):
            if k > 0:
                window_sum = window_sum - code[i] + code[(i + k) % n]
            else:
                # add new leftmost (Previous element) and remove 
                window_sum = window_sum - code[(i + k - 1) % n] + code[i - 1]
            
            res[i] = window_sum
        
        return res
```

#### Step 1: Initialize First Window
For `k > 0`: Calculate sum of elements `code[1]` to `code[k]` (next k elements after index 0)
For `k < 0`: Calculate sum of elements `code[k:]` (last |k| elements, which are "previous" to index 0 in circular array)

#### Step 2: Slide the Window
* For each subsequent index i from `1 to n-1`:

1. When `k > 0` (moving forward):
		* 		Remove: code[i] (element that was at the start of previous window)
		* 		Add: `code[(i + k) % n]` (new element entering the window)
2. When k < 0 (moving backward):
		* 	Remove: `code[(i + k - 1) % n]` (rightmost element leaving the previous window)
		* 	Add: `code[i - 1]` (new leftmost element entering the window)

