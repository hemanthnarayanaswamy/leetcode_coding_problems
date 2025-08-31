<h2><a href="https://leetcode.com/problems/maximum-number-of-balls-in-a-box">1844. Maximum Number of Balls in a Box</a></h2><h3>Easy</h3><hr><p>You are working in a ball factory where you have <code>n</code> balls numbered from <code>lowLimit</code> up to <code>highLimit</code> <strong>inclusive</strong> (i.e., <code>n == highLimit - lowLimit + 1</code>), and an infinite number of boxes numbered from <code>1</code> to <code>infinity</code>.</p>

<p>Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball&#39;s number. For example, the ball number <code>321</code> will be put in the box number <code>3 + 2 + 1 = 6</code> and the ball number <code>10</code> will be put in the box number <code>1 + 0 = 1</code>.</p>

<p>Given two integers <code>lowLimit</code> and <code>highLimit</code>, return<em> the number of balls in the box with the most balls.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lowLimit = 1, highLimit = 10
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lowLimit = 5, highLimit = 15
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lowLimit = 19, highLimit = 28
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= lowLimit &lt;= highLimit &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digitSum(num):
            tmp = [int(d) for d in str(num)]
            return sum(tmp)

        ballBox = {}
        maxBalls = 0

        for i in range(lowLimit, highLimit+1):
            box = digitSum(i)
            ballBox[box] = ballBox.get(box, 0) + 1
            if ballBox[box] > maxBalls:
                maxBalls = ballBox[box]
        
        return maxBalls
```
---
```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        ballBox = {}
        maxBalls = 0

        for i in range(lowLimit, highLimit+1):
            box = digitSum(i)
            ballBox[box] = ballBox.get(box, 0) + 1
            if ballBox[box] > maxBalls:
                maxBalls = ballBox[box]
        
        return maxBalls
```
---
# Optimal Solution
```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        LIMIT = 45  # 1 <= input <= 10 ** 5, implies sum of digits <= 45
        count = [0] * (LIMIT + 1)

        for x in range(lowLimit, highLimit + 1):
            digit_sum = 0
            while x:
                digit_sum += x % 10
                x //= 10
            
            count[digit_sum] += 1
        
        return max(count)
```

## Problem Statement
- Given a range of numbers from `lowLimit` to `highLimit`
- Each number is placed in a box based on the sum of its digits
- Find the maximum number of balls in any single box

## Solution Approach

### Key Insight: Digit Sum as Box Number
Each ball (number) goes into a box numbered by its digit sum.

### Algorithm Components

#### 1. Digit Sum Function
```python
def digitSum(num):
    tmp = [int(d) for d in str(num)]
    return sum(tmp)
```
- Converts number to string to access individual digits
- Converts each digit back to integer
- Returns sum of all digits

#### 2. Main Algorithm
```python
ballBox = {}        # Dictionary to count balls per box
maxBalls = 0        # Track maximum balls in any box

for i in range(lowLimit, highLimit+1):
    box = digitSum(i)                    # Calculate box number
    ballBox[box] = ballBox.get(box, 0) + 1   # Increment count
    if ballBox[box] > maxBalls:          # Update maximum
        maxBalls = ballBox[box]
```

### Data Structures Used
- **Dictionary (`ballBox`)**: Maps box number → count of balls
- **Integer (`maxBalls`)**: Tracks the highest count seen so far

## Example Walkthrough

### Case: lowLimit=1, highLimit=10
```
Number → Digit Sum → Box → Running Count
1      → 1         → 1   → box[1] = 1
2      → 2         → 2   → box[2] = 1
3      → 3         → 3   → box[3] = 1
4      → 4         → 4   → box[4] = 1
5      → 5         → 5   → box[5] = 1
6      → 6         → 6   → box[6] = 1
7      → 7         → 7   → box[7] = 1
8      → 8         → 8   → box[8] = 1
9      → 9         → 9   → box[9] = 1
10     → 1+0=1     → 1   → box[1] = 2  ← Maximum!

Result: 2 (box 1 has the most balls)
```

### Case: lowLimit=5, highLimit=15
```
5→5, 6→6, 7→7, 8→8, 9→9, 10→1, 11→2, 12→3, 13→4, 14→5, 15→6

Box counts:
box[1] = 1 (from 10)
box[2] = 1 (from 11)  
box[3] = 1 (from 12)
box[4] = 1 (from 13)
box[5] = 2 (from 5, 14)  ← Maximum!
box[6] = 2 (from 6, 15)  ← Maximum!
box[7] = 1 (from 7)
box[8] = 1 (from 8)
box[9] = 1 (from 9)

Result: 2
```

