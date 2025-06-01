<h2><a href="https://leetcode.com/problems/find-the-integer-added-to-array-i">3397. Find the Integer Added to Array I</a></h2><h3>Easy</h3><hr><p>You are given two arrays of equal length, <code>nums1</code> and <code>nums2</code>.</p>

<p>Each element in <code>nums1</code> has been increased (or decreased in the case of negative) by an integer, represented by the variable <code>x</code>.</p>

<p>As a result, <code>nums1</code> becomes <strong>equal</strong> to <code>nums2</code>. Two arrays are considered <strong>equal</strong> when they contain the same integers with the same frequencies.</p>

<p>Return the integer <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">nums1 = [2,6,4], nums2 = [9,7,5]</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The integer added to each element of <code>nums1</code> is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">nums1 = [10], nums2 = [5]</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">-5</span></p>

<p><strong>Explanation:</strong></p>

<p>The integer added to each element of <code>nums1</code> is -5.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">nums1 = [1,1,1,1], nums2 = [1,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The integer added to each element of <code>nums1</code> is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length == nums2.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
	<li>The test cases are generated in a way that there is an integer <code>x</code> such that <code>nums1</code> can become equal to <code>nums2</code> by adding <code>x</code> to each element of <code>nums1</code>.</li>
</ul>

# solution 
* The array is shuffled and but still the elements of num1 are equal to num2 array if the x is added or removed from the elements of the num1. 
* If the elements are equal then the sum of them should be also equal 

```bash
(n1+x) + (n2+x)  + (n3+x) = 3x(n1 + n2 + n3)

here the 3 is lenght of the array nusm1 

apart from that 3x the sum of the num1 and num2 will be equal 

x = (sum(num2) - sum(num1)) // len(num1)
```
```python
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        n = len(nums1)
        
        return (s2 - s1) // n
```

```python
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)
```

```python
class Solution:
    def addedInteger(self, n1: List[int], n2: List[int]) -> int:
        return min(n2) - min(n1)
```

