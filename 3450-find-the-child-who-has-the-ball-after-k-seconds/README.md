<h2><a href="https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds">3450. Find the Child Who Has the Ball After K Seconds</a></h2><h3>Easy</h3><hr><p>You are given two <strong>positive</strong> integers <code>n</code> and <code>k</code>. There are <code>n</code> children numbered from <code>0</code> to <code>n - 1</code> standing in a queue <em>in order</em> from left to right.</p>

<p>Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches <strong>either</strong> end of the line, i.e. child 0 or child <code>n - 1</code>, the direction of passing is <strong>reversed</strong>.</p>

<p>Return the number of the child who receives the ball after <code>k</code> seconds.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Time elapsed</th>
			<th>Children</th>
		</tr>
		<tr>
			<td><code>0</code></td>
			<td><code>[<u>0</u>, 1, 2]</code></td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td><code>[0, <u>1</u>, 2]</code></td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td><code>[0, 1, <u>2</u>]</code></td>
		</tr>
		<tr>
			<td><code>3</code></td>
			<td><code>[0, <u>1</u>, 2]</code></td>
		</tr>
		<tr>
			<td><code>4</code></td>
			<td><code>[<u>0</u>, 1, 2]</code></td>
		</tr>
		<tr>
			<td><code>5</code></td>
			<td><code>[0, <u>1</u>, 2]</code></td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Time elapsed</th>
			<th>Children</th>
		</tr>
		<tr>
			<td><code>0</code></td>
			<td><code>[<u>0</u>, 1, 2, 3, 4]</code></td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td><code>[0, <u>1</u>, 2, 3, 4]</code></td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td><code>[0, 1, <u>2</u>, 3, 4]</code></td>
		</tr>
		<tr>
			<td><code>3</code></td>
			<td><code>[0, 1, 2, <u>3</u>, 4]</code></td>
		</tr>
		<tr>
			<td><code>4</code></td>
			<td><code>[0, 1, 2, 3, <u>4</u>]</code></td>
		</tr>
		<tr>
			<td><code>5</code></td>
			<td><code>[0, 1, 2, <u>3</u>, 4]</code></td>
		</tr>
		<tr>
			<td><code>6</code></td>
			<td><code>[0, 1, <u>2</u>, 3, 4]</code></td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<table>
	<tbody>
		<tr>
			<th>Time elapsed</th>
			<th>Children</th>
		</tr>
		<tr>
			<td><code>0</code></td>
			<td><code>[<u>0</u>, 1, 2, 3]</code></td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td><code>[0, <u>1</u>, 2, 3]</code></td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td><code>[0, 1, <u>2</u>, 3]</code></td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/pass-the-pillow/description/" target="_blank"> 2582: Pass the Pillow.</a></p>

# Ball Passing Problem - Solution Notes

## Problem Statement
- **n** children numbered 0 to n-1 standing in a line
- Ball starts at child 0, moving right
- Direction reverses when ball reaches either end (child 0 or n-1)
- Find which child has the ball after **k** seconds

## Solution Approach

### Key Insight: Cyclic Pattern
The ball follows a repeating pattern due to direction reversals at the ends.

### Pattern Analysis
For n children (0 to n-1):
- **Forward path**: 0 → 1 → 2 → ... → (n-1)  [takes n-1 steps]
- **Backward path**: (n-1) → (n-2) → ... → 1 → 0  [takes n-1 steps]
- **Total cycle length**: 2(n-1) steps

### Algorithm Steps

```python
def numberOfChild(n, k):
    n -= 1              # Convert to cycle length
    m = k % n           # Position within half-cycle
    q = k // n          # Number of complete half-cycles
    
    if q % 2:           # Odd half-cycles = moving backward
        return n - m 
    else:               # Even half-cycles = moving forward
        return m
```

### Variable Meanings
- **n**: After `n -= 1`, represents the cycle length (n-1)
- **m**: Remainder when k is divided by cycle length
- **q**: Number of complete half-cycles completed
- **q % 2**: Determines direction (even = forward, odd = backward)

### Direction Logic
- **Even q** (0, 2, 4, ...): Ball moving forward → return `m`
- **Odd q** (1, 3, 5, ...): Ball moving backward → return `n - m`

## Example Walkthrough

### Case: n=5, k=6
```
Children: 0, 1, 2, 3, 4
Ball movement: 0→1→2→3→4→3→2

Step-by-step:
- n = 5-1 = 4 (cycle length)
- m = 6 % 4 = 2 (position in half-cycle)
- q = 6 // 4 = 1 (one complete half-cycle)
- q is odd → moving backward
- Result: 4 - 2 = 2 ✓
```

### Manual Trace Verification
```
k=0: child 0
k=1: child 1  
k=2: child 2
k=3: child 3
k=4: child 4 (reaches end, direction reverses)
k=5: child 3
k=6: child 2 ✓
```

## Edge Cases to Consider

1. **k=0**: Should return 0 (starting position)
2. **k < n-1**: Ball hasn't reached the end yet
3. **Large k**: Algorithm handles efficiently with modular arithmetic

## Time & Space Complexity
- **Time**: O(1) - constant time operations
- **Space**: O(1) - only using a few variables

## Key Takeaways
1. Recognize the cyclic pattern in back-and-forth movement
2. Use modular arithmetic to avoid simulating each step
3. Track direction using even/odd cycle counts
4. The effective cycle length is 2(n-1), but we use (n-1)

```python
def numberOfChild(n, k):
    n -= 1
    m = k % n
    q = k // n

    if q % 2:
        return n - m 
    else:
        return m
```
