<h2><a href="https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/">2668. Form Smallest Number From Two Digit Arrays</a></h2><h3>Easy</h3><hr>Given two arrays of <strong>unique</strong> digits <code>nums1</code> and <code>nums2</code>, return <em>the <strong>smallest</strong> number that contains <strong>at least</strong> one digit from each array</em>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,1,3], nums2 = [5,7]
<strong>Output:</strong> 15
<strong>Explanation:</strong> The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [3,5,2,6], nums2 = [3,1,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The number 3 contains the digit 3 which exists in both arrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 9</code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 9</code></li>
	<li>All digits in each array are <strong>unique</strong>.</li>
</ul>

# Solution 
```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        commonNums = set(nums1) & set(nums2)

        if commonNums:
            return min(commonNums)

        min1 = min(nums1)
        min2 = min(nums2)

        if min1 < min2:
            return min1 * 10 + min2
        else:
            return min2 * 10 + min1
```
---
```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        commonNums = set(nums1) & set(nums2)

        if commonNums:
            return min(commonNums)

        min1 = min(nums1)
        min2 = min(nums2)

        if min2 < min1:
            min1, min2 = min2, min1

        return min1 * 10 + min2
```
---
```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        commonNums = set(nums1) & set(nums2)

        if commonNums:
            return min(commonNums)

        n1 = min(nums1)
        n2 = min(nums2)

        return min(n1, n2) * 10 + max(n1, n2)
```
