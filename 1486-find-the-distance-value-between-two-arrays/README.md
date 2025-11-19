<h2><a href="https://leetcode.com/problems/find-the-distance-value-between-two-arrays">1486. Find the Distance Value Between Two Arrays</a></h2><h3>Easy</h3><hr><p>Given two integer arrays <code>arr1</code> and <code>arr2</code>, and the integer <code>d</code>, <em>return the distance value between the two arrays</em>.</p>

<p>The distance value is defined as the number of elements <code>arr1[i]</code> such that there is not any element <code>arr2[j]</code> where <code>|arr1[i]-arr2[j]| &lt;= d</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
For arr1[0]=4 we have: 
|4-10|=6 &gt; d=2 
|4-9|=5 &gt; d=2 
|4-1|=3 &gt; d=2 
|4-8|=4 &gt; d=2 
For arr1[1]=5 we have: 
|5-10|=5 &gt; d=2 
|5-9|=4 &gt; d=2 
|5-1|=4 &gt; d=2 
|5-8|=3 &gt; d=2
For arr1[2]=8 we have:
<strong>|8-10|=2 &lt;= d=2</strong>
<strong>|8-9|=1 &lt;= d=2</strong>
|8-1|=7 &gt; d=2
<strong>|8-8|=0 &lt;= d=2</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= arr1[i], arr2[j] &lt;= 1000</code></li>
	<li><code>0 &lt;= d &lt;= 100</code></li>
</ul>

# Approach 
* You're supposed to count the elements in `arr1` that do NOT yield a value `<= d` when any element from `arr2` is subtracted from it. To explain the example;
```ini
arr1[0] = 4 doesn't violate the condition. Hence, we count it.
arr1[1] = 5 also doesn't violate the condition. We also count it, bringing our count to two.
arr1[8] = 8 violates the condition, so it isn't counted.
```
**Since that's the end of `arr1`, the total number of GOOD numbers we have is `2`. That's why the output is `2`**
```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = len(arr1)

        for a1 in arr1:
            for a2 in arr2:
                if abs(a1 - a2) <= d:
                    res -= 1
                    break
        
        return res
```
---
# Binary Search Solution 
* The `arr2` array is sorted for binary search.
* We assume all the numbers are good in `arr1`, `ans=len(arr1)`. 
* Now we use binary seach to check elements in the sorted array `arr2`. For a the `mid` with `diff=abs(arr2[m]-i)`, ` if diff<=d:` then we break and reduce the result value. 
* But if the mid doesn't yeild the result, We move the pointers `r` and `l` based on the values, It like we are trying to find the minimum value in `arr2` which may violate the condition. 

```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int: 
        arr2.sort()
        ans=len(arr1)

        for i in arr1:
            l, r = 0, len(arr2)-1

            while l<=r:
                m=(l+r)//2
                diff=abs(arr2[m]-i)

                if diff<=d:
                    ans -= 1
                    break
                if arr2[m] > i:
                    r = m-1
                else:
                    l = m+1

        return ans
```
