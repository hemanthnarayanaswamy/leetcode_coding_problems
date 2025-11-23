<h2><a href="https://leetcode.com/problems/check-if-any-element-has-prime-frequency">3914. Check if Any Element Has Prime Frequency</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>Return <code>true</code> if the frequency of any element of the array is <strong>prime</strong>, otherwise, return <code>false</code>.</p>

<p>The <strong>frequency</strong> of an element <code>x</code> is the number of times it occurs in the array.</p>

<p>A prime number is a natural number greater than 1 with only two factors, 1 and itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>4 has a frequency of two, which is a prime number.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements have a frequency of one.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,2,4,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Both 2 and 4 have a prime frequency.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
* Have a set with all prime numbers. 
```python
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        numsFreq = Counter(nums)

        for num, freq in numsFreq.items():
            if freq in prime:
                return True
        
        return False
```

# Check Prime 
* To check if the number is prime, We need to check the modulo of the number from `2, sqrt(n)`

```python
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        for count in counts.values():
            if is_prime(count):
                return True
        
        return False
```
