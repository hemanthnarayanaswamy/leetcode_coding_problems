<h2><a href="https://leetcode.com/problems/contiguous-array">525. Contiguous Array</a></h2><h3>Medium</h3><hr><p>Given a binary array <code>nums</code>, return <em>the maximum length of a contiguous subarray with an equal number of </em><code>0</code><em> and </em><code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

### STEPS to Solve 

1. WE'll calculate the prefix sum by consider 0 value to be -1 that way when the sum is zero there are equal number of ones and zeros 
2. We'll use a hash map to keep track of all the length of sub array of the prefix sum { prefix_sum: first occurance of prefix sum detected }
3. Main Idea to use hash map is to store first occurance of the prefix sum 
4. We need to only store the prefix sum if it doesn't exit in the hashmap
5. 
```python
prefix_sum += 1 if nums[i] == 1 else -1
if prefix_sum not in sum_track:
         sum_track[prefix_sum] = i
```
6. We need to calculate the maximum length when the prefix sum is seen again, when the prefix_sum repeats that means the subarray in between is balanced 
* Example: [0, 1, 1, 0, 1, 1, 0, 0] here predix_sum = [ -1, 0, 1, 0, 1, 2, 1, 0 ] sum 0 occures at index (1, 3, 7) meaning (0 to 1) (0 to 3) and (0 to 7) subarray is balanced, 
* * Example 2: [1,0,0,0,1,1,1,0] prefix_sum = [1, 0, -1, -2, -1, 0, 1, 0] if you see here at index(0, 6) value is 1 that means from (0 to 6) length 6 subarray exits with equal number of 1st and zeros. 
7. If the prefix sum repeats we need to calculate the max_lenght of that sub array using the formula `i - sum_track[prefix_sum]`


#### My first Solution 
* I understood and wrote a proper solution but so edge cases didn't pass, Time - 92ms and Memeory 23.55 MB
```python
sum_track = {} ## {prefix_sum: length Of subarray}
        prefix_sum = 0 ## To keep TRack of prefix sum 
        max_subarray_length = 0 ## Keeping track of subarray length 

        for i in range(len(nums)):
            prefix_sum += 1 if nums[i] == 1 else -1

            if prefix_sum not in sum_track:
                sum_track[prefix_sum] = i
            else: 
                max_subarray_length = max(max_subarray_length, i - sum_track[prefix_sum])
        
        return max_subarray_length
```
* A small error When initializing the hashmap we need to `{-1: 0}`, If `prefix_sum ==0` at any point, it means the entire subarray from the index 0 to i is balanced 
* If the {0: -1} is missing, it'll not count the case correctly

### Optimized solution 

```python 
def findMaxLength(self, nums: List[int]) -> int:
        sum_track = {0: -1} ## {prefix_sum: irst occurance of prefix sum detected}
        prefix_sum = 0 ## To keep TRack of prefix sum 
        max_subarray_length = 0 ## Keeping track of subarray length whenever we detect the prefix sum again

        nums_length = len(nums)
## we are checking if the number of zeros are equal to number of ones if half of the length of the array is equal to sum of the array then we can return the length of the array
        if nums_length/2 == sum(nums): 
                return nums_length

        for i in range(nums_length):
            prefix_sum += 1 if nums[i] == 1 else -1

            if prefix_sum not in sum_track:
                sum_track[prefix_sum] = i
            else: 
                first_occurence = sum_track[prefix_sum]
                if max_subarray_length < i - first_occurence:
                    max_subarray_length =  i - first_occurence
        
        return max_subarray_length
```
* We are checking for a edge case if number of ones are zeros are equal using the length divide by 2 
* instead of using the max function we are using the if condition to proceed only when it is less that way we are saving time
