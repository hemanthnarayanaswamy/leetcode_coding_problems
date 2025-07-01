<h2><a href="https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations">2525. Count Number of Distinct Integers After Reverse Operations</a></h2><h3>Medium</h3><hr><p>You are given an array <code>nums</code> consisting of <strong>positive</strong> integers.</p>

<p>You have to take each integer in the array, <strong>reverse its digits</strong>, and add it to the end of the array. You should apply this operation to the original integers in <code>nums</code>.</p>

<p>Return <em>the number of <strong>distinct</strong> integers in the final array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,13,10,12,31]
<strong>Output:</strong> 6
<strong>Explanation:</strong> After including the reverse of each number, the resulting array is [1,13,10,12,31,<u>1,31,1,21,13</u>].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After including the reverse of each number, the resulting array is [2,2,2,<u>2,2,2</u>].
The number of distinct integers in this array is 1 (The number 2).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>

# Solution 
* Use set to store all the distinct intergers 

```python
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        def reversedIntegers(num):
            x = 0
            while num:
                digit = num % 10 # Extract the last digit 
                x = 10 * x + digit
                num //= 10  # Remove last digit from num
            return x

        distinctInt = set()

        for num in nums:
            rev = reversedIntegers(num)
            distinctInt.add(num)
            distinctInt.add(rev)
        
        return len(distinctInt)
```

* Remove the helper function and directly use the string reverse method to add the integers. 

```python
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinctInt = set(nums)

        for num in nums:
            rev = int(str(num)[::-1])
            distinctInt.add(rev)
        
        return len(distinctInt)
```

# Optimal Solution 
```ini 
* you skip the str(num)[::-1] and int(...) entirely for any num < 10.  That can easily halve (or better) your string‐conversion work if your input has a lot of single‐digit values.
* Each call to .add() on a Python set has to recompute the element’s hash, check for membership, etc.  By instead:
	1.	Collecting everything in a list (distinctInt = nums[:] + .append() calls)
	2.	Then calling set(distinctInt) just once

you push all of that hashing and membership‐checking work into a single bulk operation, which is heavily optimized in C and benefits from knowing the final size in advance.  You avoid the repeated overhead of individual .add() calls inside your loop.
```

```python
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinctInt = nums[::]

        for num in nums:
            if num > 9:
                distinctInt.append(int(str(num)[::-1]))
        
        return len(set(distinctInt))
```
