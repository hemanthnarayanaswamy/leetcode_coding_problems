<h2><a href="https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals">1604. Least Number of Unique Integers after K Removals</a></h2><h3>Medium</h3><hr><p>Given an array of integers&nbsp;<code>arr</code>&nbsp;and an integer <code>k</code>.&nbsp;Find the <em>least number of unique integers</em>&nbsp;after removing <strong>exactly</strong> <code>k</code> elements<b>.</b></p>

<ol>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input: </strong>arr = [5,5,4], k = 1
<strong>Output: </strong>1
<strong>Explanation</strong>: Remove the single 4, only 5 is left.
</pre>
<strong class="example">Example 2:</strong>

<pre>
<strong>Input: </strong>arr = [4,3,1,1,3,3,2], k = 3
<strong>Output: </strong>2
<strong>Explanation</strong>: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= k&nbsp;&lt;= arr.length</code></li>
</ul>

1. To find the unique number will count using hash map.
2. how do we make sure that very less unique number remain in the arr?
      * Approach 1 - if we start deleting the number which occurs many times then will exhaust the k value, and many will still remain
      * Approach 2 - but if we start targeting the numbers in minority, then yes we can get rid of many smaller number and remaining big numbers count will be smaller anyways

# Solution
```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrFreq = Counter(arr)
        arrFreqSort = dict(sorted(arrFreq.items(), key=lambda item:item[1]))
        removeElements = 0
        countElements = 0

        for key in arrFreqSort:
            if removeElements + arrFreqSort[key] <= k:
                removeElements += arrFreqSort[key]
                countElements += 1
            else:
                temp = abs(k - removeElements)
                if arrFreqSort[key] > temp:
                    removeElements += temp
            
            if removeElements == k:
                return abs(countElements - len(arrFreqSort)
```
* The solution is bit complex as we are sorting the dictionary which is uncessary and other tracking variables are also unnecessary.

# Optimal Solution
1. sort only the values from the frequencies and get the length of that sorted array, which will indicate the total number of unique elements in the array.
2. now for each freq can be removed from k, then we increment the result count 
3. but the freq cannot to remove then it means all elements are already removed including the current one
4. Return the remaining the 

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = sorted(Counter(arr).values())  
        unique_count = len(freq) # total number of unique elements in the array
        
        for f in freq:
            if k >= f:
                k -= f
                unique_count -= 1
            else:
                break
        
        return unique_count
```
