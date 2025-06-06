<h2><a href="https://leetcode.com/problems/mean-of-array-after-removing-some-elements">1210. Mean of Array After Removing Some Elements</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>arr</code>, return <em>the mean of the remaining integers after removing the smallest <code>5%</code> and the largest <code>5%</code> of the elements.</em></p>

<p>Answers within <code>10<sup>-5</sup></code> of the <strong>actual answer</strong> will be considered accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
<strong>Output:</strong> 4.00000
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
<strong>Output:</strong> 4.77778
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>20 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>arr.length</code><b> </b><strong>is a multiple</strong> of <code>20</code>.</li>
	<li><code><font face="monospace">0 &lt;= arr[i] &lt;= 10<sup>5</sup></font></code></li>
</ul>

# Solution
```python
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()

        removeElement = int(0.05 * n)

        arrSum = sum(arr[removeElement:n-removeElement])

        return arrSum / (n - 2*removeElement)
```
* We can optimize the variable usage note the end index is `n-removeElement` but when you consider the negative indexing the value of end index will be just `-removeElement`

```python
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        n=n//20 # 5% computation 

        arr = arr[n:-n]

        return sum(arr) / len(arr)
 ```
