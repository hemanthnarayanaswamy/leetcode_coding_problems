<h2><a href="https://leetcode.com/problems/reduce-array-size-to-the-half">1464. Reduce Array Size to The Half</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>arr</code>. You can choose a set of integers and remove all the occurrences of these integers in the array.</p>

<p>Return <em>the minimum size of the set so that <strong>at least</strong> half of the integers of the array are removed</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,3,3,3,5,5,5,2,2,7]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [7,7,7,7,7,7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible set you can choose is {7}. This will make the new array empty.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>arr.length</code> is even.</li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


# Appraoch 
1. Count the frequency of each number in the array using a hash map.
2. Store all frequencies in a separate vector.
3. Sort the frequency vector in descending order.
4. Iterate through the sorted frequencies, accumulating the total number of elements removed.
5. Keep a counter to track how many unique numbers have been removed.
6. As soon as the accumulated removed elements reach at least half of the original array size, return the counter.

```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrFreq = Counter(arr)
        arrFreq = dict(sorted(arrFreq.items(), key=lambda item: item[1], reverse=True))
        n = len(arr)
        answer, counter = 0, 0

        for val in arrFreq.values():
            if answer < n // 2:
                answer += val 
                counter += 1
            elif answer > n // 2:
                return counter
        
        return counter 
```

# Improves Solution 
```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrFreq = Counter(arr)
        valueFreq = sorted(arrFreq.values(), reverse=True)
        nhalf = len(arr) // 2
        answer, counter = 0, 0

        for val in valueFreq:
            answer += val 
            counter += 1
            if answer >= nhalf:
                break
        
        return counter 
```
