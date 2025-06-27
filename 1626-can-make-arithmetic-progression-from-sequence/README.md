<h2><a href="https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence">1626. Can Make Arithmetic Progression From Sequence</a></h2><h3>Easy</h3><hr><p>A sequence of numbers is called an <strong>arithmetic progression</strong> if the difference between any two consecutive elements is the same.</p>

<p>Given an array of numbers <code>arr</code>, return <code>true</code> <em>if the array can be rearranged to form an <strong>arithmetic progression</strong>. Otherwise, return</em> <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,5,1]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,4]
<strong>Output:</strong> false
<strong>Explanation: </strong>There is no way to reorder the elements to obtain an arithmetic progression.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup> &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
</ul>

# Solution 
* Sort and array and save the diff value in the set and check the len of that set to see the result for Arithmetic Progression 

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = set()

        for i in range(1, len(arr)):
            diff.add(arr[i] - arr[i-1])
        
        return True if len(diff) == 1 else False
```

# Improved Solution 
```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arrSorted = sorted(arr)

        diffval = arrSorted[1] - arrSorted[0]

        for i in range(2, len(arrSorted)):
            if arrSorted[i] - arrSorted[i-1] != diffval:
                return False
        
        return True
````

# Optimal Solution 
```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        Ordered = sorted(arr)
        Target = Ordered[1] - Ordered[0]

        Cursor_A = 1
        Cursor_B = 2
        Span = len(Ordered)

        while (Cursor_B < Span):
            
            Value_A = Ordered[Cursor_A]
            Value_B = Ordered[Cursor_B]
            Difference = Value_B - Value_A

            if (Difference == Target):
                Cursor_A += 1
                Cursor_B += 1
            else:
                return False
        
        return True
```
