<h2><a href="https://leetcode.com/problems/minimum-absolute-difference">1306. Minimum Absolute Difference</a></h2><h3>Easy</h3><hr><p>Given an array of <strong>distinct</strong> integers <code>arr</code>, find all pairs of elements with the minimum absolute difference of any two elements.</p>

<p>Return a list of pairs in ascending order(with respect to pairs), each pair <code>[a, b]</code> follows</p>

<ul>
	<li><code>a, b</code> are from <code>arr</code></li>
	<li><code>a &lt; b</code></li>
	<li><code>b - a</code> equals to the minimum absolute difference of any two elements in <code>arr</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,2,1,3]
<strong>Output:</strong> [[1,2],[2,3],[3,4]]
<strong>Explanation: </strong>The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,6,10,15]
<strong>Output:</strong> [[1,3]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,8,-10,23,19,-4,-14,27]
<strong>Output:</strong> [[-14,-10],[19,23],[23,27]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
</ul>


# Solution
* Initiate the minDiff to infinity and then in one single loop, after sorting compute the diff and keep appending then check 
* if something less then the minDiff arise clear the result and append that pair and update that as minDiff for next iterations

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif=9999
        res=[]
        for i in range(len(arr)-1):
            min_dif=min(min_dif,abs(arr[i]-arr[i+1]))
            if min_dif==1:
                break
        for i in range(len(arr)-1):
            if min_dif==(arr[i+1]-arr[i]):
                res.append([arr[i],arr[i+1]])
        return res
```

## Improved Solution 
* instead of clear reinitialize the array with the new elements 
```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        result = []

        for i in range(len(arr)-1):
            a, b = arr[i], arr[i+1]
            tempDiff = abs(b - a)
            
            if tempDiff < minDiff:
                minDiff = tempDiff
                result = [[a, b]]

            elif tempDiff == minDiff:
                 result.append([a, b])
                
        return result 
```
				
