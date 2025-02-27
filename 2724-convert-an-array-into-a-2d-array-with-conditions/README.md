<h2><a href="https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions">2724. Convert an Array Into a 2D Array With Conditions</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>. You need to create a 2D array from <code>nums</code> satisfying the following conditions:</p>

<ul>
	<li>The 2D array should contain <strong>only</strong> the elements of the array <code>nums</code>.</li>
	<li>Each row in the 2D array contains <strong>distinct</strong> integers.</li>
	<li>The number of rows in the 2D array should be <strong>minimal</strong>.</li>
</ul>

<p>Return <em>the resulting array</em>. If there are multiple answers, return any of them.</p>

<p><strong>Note</strong> that the 2D array can have a different number of elements on each row.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,4,1,2,3,1]
<strong>Output:</strong> [[1,3,4,2],[1,3],[1]]
<strong>Explanation:</strong> We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [[4,3,2,1]]
<strong>Explanation:</strong> All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
</ul>

## Solution Approach 
* This solution is not covering many edge cases as such `[8,8,8,8,2,4,4,2,4]` my output is `[[8],[8],[8],[8,2,4],[4,2],[4]]` but expected output `[[8,4,2],[8,4,2],[8,4],[8]]`
```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        for num in nums:
            if num not in temp:
                temp.append(num)
            else:
                result.append(temp.copy())
                temp.clear()
                temp.append(num)
        result.append(temp)
        return result
```

* Not correctly handling multiple duplicates of a number.
* Clearing temp too early, causing elements to be lost.
* Not dynamically adjusting rows when an element appears multiple times.

### Improved Solution 
* We track the counter for each occurance of that number and use the tracker number as a row number that need to append to.

```
[1,3,4,1,2,3,1,8,9]
- 1 --> Initially count is 1 so initialize to 0 and check than get the index of that number
      --> Len(result) is 0 which is equal to index so we need a new row to append it 
			--> we create a new row in result and append element and increment its index to 1
- 1 --> Now when 1 is encountered, the index is 1 as it was encountered earlier 
     --> len(result) = 1 and so the index of num so we create a new row for it and append that element there 
		 --> and increment the count of that again 
```

* As we iterate through nums, for each element, we check if it's the first occurrence. If it is, we initialize its count in count_nums. Then, we use the count of the element as an index idx to determine which row of ans it should go into. If idx is equal to the current number of rows in ans, it means we need a new row for this occurrence of the element. We then append the element to the appropriate row.

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count_freq = {}  ## To store the frequencey {1: 3, 3: 2, 4: 1, 2: 1, 8: 1, 9: 1}
        result = []

        for num in nums:
				    # If the number is not in count_nums, initialize it with 0****
            if num not in count_freq:
                count_freq[num] = 0
            
						# Get the current count of num, which will be the index in ans
            idx = count_freq[num]
						
						# If idx is equal to the length of ans, it means we need a new row
            if idx >= len(result):
                result.append([])
            # Add the number to the row in ans at index idx
            result[idx].append(num)
						
						# Increment the count of num in count_nums
            count_freq[num] += 1
        return result
```

## Optimized Solution 

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        rows = [[] for _ in range(max(freq.values()))]
        
        for num, count in freq.items():
            for i in range(count):
                rows[i].append(num)
        
        return rows
```

