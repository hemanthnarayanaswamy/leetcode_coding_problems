<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty">3094. Minimum Number of Operations to Make Array Empty</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array <code>nums</code> consisting of positive integers.</p>

<p>There are two types of operations that you can apply on the array <strong>any</strong> number of times:</p>

<ul>
	<li>Choose <strong>two</strong> elements with <strong>equal</strong> values and <strong>delete</strong> them from the array.</li>
	<li>Choose <strong>three</strong> elements with <strong>equal</strong> values and <strong>delete</strong> them from the array.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations required to make the array empty, or </em><code>-1</code><em> if it is not possible</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,3,2,2,4,2,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,2,2,3,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to empty the array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/" target="_blank">2244: Minimum Rounds to Complete All Tasks.</a></p>

## Solution Approach 

* `% (modulo)` gives you the Remainder and `// (floor division)` gives you the Quotient.

### My Approach to Solution 
1. Use Hash map to get the Frequency of the numbers and store it 
2. Iterate through the keys to check the value is zero for modulo of 2 or 3.
3. Use counter to store the quotient to store how many operations are required to remove it completely 
4. Than if any key is not zero through modulo return -1 else the counter 

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        nums_map = {}
        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        for num in nums_map:
            result_mod_2 = nums_map[num] % 2
            result_mod_3 = nums_map[num] % 3
            if result_mod_2 != 0 and result_mod_3 != 0:
                return -1
            elif result_mod_2 == 0 and result_mod_3 == 0:
                result += min(nums_map[num] // 2, nums_map[num] // 3)
            elif result_mod_2 == 0 and result_mod_3 != 0:
                result += nums_map[num] // 2
            else:
                result += nums_map[num] // 3

        return result
```
- Some problem with the solution is it is not efficient example `[14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]` answer is 7 but mine doing it in 8. 
- So need to improve the solution to first check only mod-3 than go to others
```
occurrence of a number is 1
occurrence of a number % 3 == 0
occurrence of a number % 3 == 1 than result += nums_map[num] // 3 + 1
occurrence of a number % 3 == 2 then result += nums_map[num] // 3 + 1

Because 
10 % 3 = 1
3*3 + 2*0 + 1 = 10 --- 10 // 3 = 3 but efficient is 6// 3=2 and 4//2 == 2 result = 4 
3*2 + 2*2 = 10 ## Meaning so we need to add one to equate the result `nums_map[num] // 3 + 1`

Similarly 10 % 3 = 2 
means the remainder can be divisible by 2 
2 // 2 is 1 so we are adding 1 
```

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        nums_map = {}
        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        for num in nums_map:
            result_mod_3 = nums_map[num] % 3
            if nums_map[num] // 3 == 0 and nums_map[num] //2 == 0:  ## Checking if the freq of the num is 1 if yes return -1 
                return -1
            elif result_mod_3 == 0: ## We are only checking for mod 3 
                result += nums_map[num] // 3
            elif result_mod_3 == 1 or result_mod_3 == 2:  ## Look in above explaination 
                result += nums_map[num] // 3 + 1

        return result ## Returning the result 
```

### Optimized Solution 
1. Instead of division check if the frequency is 1
```
if nums_map[num] // 3 == 0 and nums_map[num] // 2 == 0:
  to 
if nums_map[num] == 1:
    return -1
```

2. No need to explit this condition 
```python
if result_mod_3 == 1 or result_mod_3 == 2:
     result += nums_map[num] // 3 + 1
```
3. Final Optimal Solution

```python
from collections import Counter

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        result = 0
        nums_map = Counter(nums)  # Using Counter for frequency counting

        for num, count in nums_map.items():
            if count == 1:  # If only one occurrence, it's impossible
                return -1

            quotient = count // 3  # Number of full groups of 3
            remainder = count % 3  # Remaining elements after grouping by 3

            if remainder == 0:
                result += quotient  # Perfectly divisible by 3
            else:
                result += quotient + 1  # Need one extra operation (either a group of 2 or extra 3)

        return result
```


