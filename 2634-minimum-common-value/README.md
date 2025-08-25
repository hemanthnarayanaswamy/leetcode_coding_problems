<h2><a href="https://leetcode.com/problems/minimum-common-value">2634. Minimum Common Value</a></h2><h3>Easy</h3><hr><p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in non-decreasing order, return <em>the <strong>minimum integer common</strong> to both arrays</em>. If there is no common integer amongst <code>nums1</code> and <code>nums2</code>, return <code>-1</code>.</p>

<p>Note that an integer is said to be <strong>common</strong> to <code>nums1</code> and <code>nums2</code> if both arrays have <strong>at least one</strong> occurrence of that integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3], nums2 = [2,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The smallest element common to both arrays is 2, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,6], nums2 = [2,3,4,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
	<li>Both <code>nums1</code> and <code>nums2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>

# Solution 
* We need to return the minimum common element between the two arrays. 
**We need to return the first element that we encounter in both arrays.** 
* Since the arrays are sorted in non Decreasing Order whatever the first element we encounger will be the minimum element. 
```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i = j = 0

        if nums1[-1] < nums2[0]:
            return -1

        while i < n1  and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return -1
```
---
```python
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0

        while i < n1  and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return -1
```
* Both arrays are sorted in non-decreasing order
* Use two pointers to traverse both arrays simultaneously
* Always advance the pointer pointing to the smaller element

```ini
# If nums1[i] == nums2[j]: Found common element (return immediately)
# If nums1[i] > nums2[j]: nums2[j] is too small, advance j
# If nums1[i] < nums2[j]: nums1[i] is too small, advance i
```

```python
def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    common = set(nums1) & set(nums2)
    return min(common) if common else -1
```
