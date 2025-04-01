<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box">1895. Minimum Number of Operations to Move All Balls to Each Box</a></h2><h3>Medium</h3><hr><p>You have <code>n</code> boxes. You are given a binary string <code>boxes</code> of length <code>n</code>, where <code>boxes[i]</code> is <code>&#39;0&#39;</code> if the <code>i<sup>th</sup></code> box is <strong>empty</strong>, and <code>&#39;1&#39;</code> if it contains <strong>one</strong> ball.</p>

<p>In one operation, you can move <strong>one</strong> ball from a box to an adjacent box. Box <code>i</code> is adjacent to box <code>j</code> if <code>abs(i - j) == 1</code>. Note that after doing so, there may be more than one ball in some boxes.</p>

<p>Return an array <code>answer</code> of size <code>n</code>, where <code>answer[i]</code> is the <strong>minimum</strong> number of operations needed to move all the balls to the <code>i<sup>th</sup></code> box.</p>

<p>Each <code>answer[i]</code> is calculated considering the <strong>initial</strong> state of the boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;110&quot;
<strong>Output:</strong> [1,1,3]
<strong>Explanation:</strong> The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> boxes = &quot;001011&quot;
<strong>Output:</strong> [11,8,5,4,3,4]</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == boxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>boxes[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

# Solution Approach 
* track from left: How much of shifts you need to calculate all ones from the given index.
* do the same from right.
* return the sum of both tracks

## Brute Force Approach 
```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right_shift_sum = [0]*len(boxes)
        left_shift_sum = [0]*len(boxes)

        for i in range(len(boxes)):     # Calculate the Right Prefix
            temp_prefix = 0
            for j in range(i+1, len(boxes)):
                if boxes[j] == '1':
                    temp_prefix += (j - i)
            right_shift_sum[i] = temp_prefix
        
        for i in range(len(boxes)-1,-1,-1):   # Calculate Left Prefix 
            temp_prefix = 0
            for j in range(i-1,-1,-1):
                if boxes[j] == '1':
                    temp_prefix += (i - j)
            left_shift_sum[i] = temp_prefix
            
        return [x+y for x,y in zip(right_shift_sum, left_shift_sum)]  # Add Left and Right Prefix for the result
```

## Optimal Solution 
* Using the Prefix Sum apporach to Avoid Nested for Loops 

```python
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0]*n

        # Left to Right Prefix Operation 
        count = 0  # To track number of balls to the left
        operations = 0 # Operations required to move ball to current 

        for i in range(n):
            result[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count # Add Count to operations for the next position 

        # Right to Left Prefix Operation 
        count = 0  # To track number of balls to the right
        operations = 0 # Operations required to move ball to current 

        for i in range(n-1, -1, -1):
            result[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count # Add Count to operations for the next position 
        
        return result 
```

```python
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n
        left_balls = 0  
        right_balls = 0  
        left_cost = 0 
        right_cost = 0 
        for i in range(n):
            answer[i] = left_cost
            if boxes[i] == '1':
                left_balls += 1
            left_cost += left_balls 
        for i in range(n - 1, -1, -1):
            answer[i] += right_cost
            if boxes[i] == '1':
                right_balls += 1
            right_cost += right_balls
        return answer
```
