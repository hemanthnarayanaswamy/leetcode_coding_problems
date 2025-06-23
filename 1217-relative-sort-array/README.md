<h2><a href="https://leetcode.com/problems/relative-sort-array">1217. Relative Sort Array</a></h2><h3>Easy</h3><hr><p>Given two arrays <code>arr1</code> and <code>arr2</code>, the elements of <code>arr2</code> are distinct, and all elements in <code>arr2</code> are also in <code>arr1</code>.</p>

<p>Sort the elements of <code>arr1</code> such that the relative ordering of items in <code>arr1</code> are the same as in <code>arr2</code>. Elements that do not appear in <code>arr2</code> should be placed at the end of <code>arr1</code> in <strong>ascending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>Output:</strong> [2,2,2,1,4,3,3,9,6,7,19]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
<strong>Output:</strong> [22,28,8,6,17,44]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code></li>
	<li>All the elements of <code>arr2</code> are <strong>distinct</strong>.</li>
	<li>Each&nbsp;<code>arr2[i]</code> is in <code>arr1</code>.</li>
</ul>

# Not Recommended 
* It is a brute force solution 

1. Counter for elements in arr1 and store the result and extraNum seperately 
2. First loop with arr2 and get the freq and store that in the results array 
3. Now the elements that are not in result store them in seperate array sort them and return the addition of both arrays 

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Freq = Counter(arr1)
        result = []
        extraNum = []

        for num in arr2:
            temp = [num] * arr1Freq[num]
            result += temp 
        
        for num in arr1Freq:
            if num not in result:
                temp = [num] * arr1Freq[num]
                extraNum += temp
        
        extraNum.sort()
        
        return result + extraNum
```

# Improved Solution 
```python 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []
        
        for x in arr2:
            c = freq.pop(x, 0)
            result.extend([x] * c)
        
        leftovers = dict(sorted(freq.items(), key=lambda x:x[0]))
        
        for n, f in leftovers.items():
            result.extend([n] * f)
        
        return result
```

# Optimal Solution 
```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {x:i for i,x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))
```
