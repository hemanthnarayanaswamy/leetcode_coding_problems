<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-array-equal">1674. Minimum Operations to Make Array Equal</a></h2><h3>Medium</h3><hr><p>You have an array <code>arr</code> of length <code>n</code> where <code>arr[i] = (2 * i) + 1</code> for all valid values of <code>i</code> (i.e.,&nbsp;<code>0 &lt;= i &lt; n</code>).</p>

<p>In one operation, you can select two indices <code>x</code> and <code>y</code> where <code>0 &lt;= x, y &lt; n</code> and subtract <code>1</code> from <code>arr[x]</code> and add <code>1</code> to <code>arr[y]</code> (i.e., perform <code>arr[x] -=1 </code>and <code>arr[y] += 1</code>). The goal is to make all the elements of the array <strong>equal</strong>. It is <strong>guaranteed</strong> that all the elements of the array can be made equal using some operations.</p>

<p>Given an integer <code>n</code>, the length of the array, return <em>the minimum number of operations</em> needed to make all the elements of arr equal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>

# Solution 
* Construct the array by using the formula. 
* And create a `target` value which is median to convert all number to median we need to find the number of operations to do it. 
* for all `num < target`, we find diff between number and the target and include that in count. 
* and we ignore the `num > target` 
```python
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2*i)+1 for i in range(n)]
        count = 0
        target = sum(arr) // n

        for i in arr:
            if i < target:
                count += target - i 
        
        return count
```

## Intuition
* The array is defined as `arr[i] = 2*i + 1`, which means it contains the first n odd numbers:
`[1, 3, 5, 7, ..., 2n - 1]`
* This array is symmetric around its mean. To make all elements equal, we can redistribute values using the allowed operation: subtract 1 from one element and add 1 to another. This operation preserves the total sum.
* The target value for all elements will be the average of the array.

## Approach
You’re given an array like this:
* If n = 5, then arr = `[1, 3, 5, 7, 9]` — see the pattern?
Each number is odd and follows the rule: arr[i] = 2*i + 1.
You can do this operation:

* Pick two elements, subtract 1 from one, add 1 to the other. **Goal: make all elements equal.**
* Instead of doing operations one by one, we ask: “How many total moves will it take to balance the array?”

**Here’s the key idea:**
* The average of the array is the number we want all elements to become. For `n = 5`, the average is `5`.
* So we want to turn `[1, 3, 5, 7, 9]` into `[5, 5, 5, 5, 5]`. Now look at how far each number is from 5: `1 → 4` away, `3 → 2` away, `5 → 0`, `7 → 2`, `9 → 4`
* Total imbalance = `4 + 2 + 2 + 4 = 12`, But each operation fixes 2 units (1 from one side, 1 to the other)
* So total operations = 12 / 2 = 6
**And guess what? That’s exactly `(n * n) / 4`
* For `n = 5: (5 * 5) / 4` = `25 / 4 = 6` (rounded down)

```python
class Solution:
    def minOperations(self, n: int) -> int:
        return n*n//4
```
