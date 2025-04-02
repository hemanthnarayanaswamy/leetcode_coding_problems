<h2><a href="https://leetcode.com/problems/shuffle-the-array">1580. Shuffle the Array</a></h2><h3>Easy</h3><hr><p>Given the array <code>nums</code> consisting of <code>2n</code> elements in the form <code>[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]</code>.</p>

<p><em>Return the array in the form</em> <code>[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,1,3,4,7], n = 3
<strong>Output:</strong> [2,3,5,4,1,7] 
<strong>Explanation:</strong> Since x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 then the answer is [2,3,5,4,1,7].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,4,3,2,1], n = 4
<strong>Output:</strong> [1,4,2,3,3,2,4,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,2], n = 2
<strong>Output:</strong> [1,2,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>nums.length == 2n</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>

# Solution 
* we do a zip of two differrent ranges `(i, j)`
```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_len = len(nums)//2
        result = [0] * 2 * n
        current = 0
        
        for i,j in zip(range(0, n),range(n, 2*n)):
            result[current] = nums[i]
            current += 1
            result[current] = nums[j]
            current += 1
        
        return result
```

## Improved Solution 
```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result
```

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = [0] * len(nums)
        k = 0
        for i in range(n):
            final[k]  = nums[i]
            k += 2
        k = 1
        for i in range(n,len(nums)):
            final[k] = nums[i]
            k += 2
        return final
```
