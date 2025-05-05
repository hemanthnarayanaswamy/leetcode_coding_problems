<h2><a href="https://leetcode.com/problems/find-numbers-with-even-number-of-digits">1421. Find Numbers with Even Number of Digits</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code> of integers, return how many of them contain an <strong>even number</strong> of digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [12,345,2,6,7896]
<strong>Output:</strong> 2
<strong>Explanation: 
</strong>12 contains 2 digits (even number of digits).&nbsp;
345 contains 3 digits (odd number of digits).&nbsp;
2 contains 1 digit (odd number of digits).&nbsp;
6 contains 1 digit (odd number of digits).&nbsp;
7896 contains 4 digits (even number of digits).&nbsp;
Therefore only 12 and 7896 contain an even number of digits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [555,901,482,1771]
<strong>Output:</strong> 1 
<strong>Explanation: </strong>
Only 1771 contains an even number of digits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


# Solution 

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Counter to count the number of even digit integers
        even_digit_count = 0

        for num in nums:
            # Compute the number of digits in num
            digit_count = int(math.floor(math.log10(num))) + 1
            if digit_count % 2 == 0:
                even_digit_count += 1

        return even_digit_count
```
```
Let N be the length of nums, which represents the number of integers for which we have to check.
Let M be the maximum integer in nums.

Time complexity: O(N⋅logM)
```

## Optimal Solution
```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Counter to count the number of even digit integers
        even_digit_count = 0

        for num in nums:
            if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or num == 100000:
                even_digit_count += 1

        return even_digit_count
```
