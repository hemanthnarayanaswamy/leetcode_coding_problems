<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">347. Top K Frequent Elements</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,2,2,3], k = 2
<strong>Output:</strong> [1,2]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>k</code> is in the range <code>[1, the number of unique elements in the array]</code>.</li>
	<li>It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Your algorithm&#39;s time complexity must be better than <code>O(n log n)</code>, where n is the array&#39;s size.</p>

## Solution Approach 
* Get the Frequency of the Elements with the counter module and sort the dict by value using the `sorted and lambda` functions.
* Than try to append that many as K elements into the result 
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums)
        ## Sorting the Dictionary by the values 
        ## {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        nums_freq = {k: v for k, v in sorted(nums_freq.items(), reverse = True, key=lambda item: item[1])} 
				#  Sorting the Dict in reverse based on the dict.values not keys  
        result = []
        for keys in nums_freq:
            result.append(keys)
            k -= 1
            if k == 0:
                return result 
        return result
```

```python
nums_freq = {k: v for k, v in sorted(nums_freq.items(), reverse = True, key=lambda item: item[1])}
```
* Sorting the Dict with values using the Lambda function 
       
