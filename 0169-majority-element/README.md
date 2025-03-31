<h2><a href="https://leetcode.com/problems/majority-element">169. Majority Element</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>&lfloor;n / 2&rfloor;</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

#### My approach 
1. define the dict 
2. iterrate through the array and if the element in dict add one and check if that value if > than n/2 and so 
3. This is the solution based off my approach 
```python 
from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
    
        nums = Counter(nums)

        for key, value in nums.items():
            if value > n // 2:
                return key
```
4. Optimal solution 
```python 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi=len(nums)//2
        for i in set(nums):
            if nums.count(i)>maxi:
                return i
```


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sam=Counter(nums)
        sor=sorted(sam.items(), key=lambda x:x[1], reverse=True)
        return (sor[0][0])
```
