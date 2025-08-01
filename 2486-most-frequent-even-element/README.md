<h2><a href="https://leetcode.com/problems/most-frequent-even-element">2486. Most Frequent Even Element</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return <em>the most frequent even element</em>.</p>

<p>If there is a tie, return the <strong>smallest</strong> one. If there is no such element, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2,2,4,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,4,4,9,2,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 is the even element appears the most.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [29,47,21,41,13,37,25,7]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no even element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
* Check if its a even number then the maxFreq and the current Freq are equal then store the minimum values of the even numbers.
* if current freq is greater then the maxFreq then replace maxFreq with current freq and result with the current number, Return the Result 

```python
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        result, mostFreq = -1, -1
        
        for num, freq in Counter(nums).items():
            if num % 2 == 0:
                if freq == mostFreq:
                    result = min(result, num)
                elif freq > mostFreq:
                    mostFreq = freq
                    result = num
        
        return result
```

# Improved Solution 
```python
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        result, mostFreq = -1, -1

        evenNum = [num for num in nums if num % 2 == 0]
        
        for num, freq in Counter(evenNum).items():
                if freq == mostFreq:
                    result = min(result, num)
                elif freq > mostFreq:
                    mostFreq = freq
                    result = num
        return result
```
