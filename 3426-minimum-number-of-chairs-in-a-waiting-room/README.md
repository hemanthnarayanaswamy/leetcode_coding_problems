<h2><a href="https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room">3426. Minimum Number of Chairs in a Waiting Room</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code>. Simulate events at each second <code>i</code>:</p>

<ul>
	<li>If <code>s[i] == &#39;E&#39;</code>, a person enters the waiting room and takes one of the chairs in it.</li>
	<li>If <code>s[i] == &#39;L&#39;</code>, a person leaves the waiting room, freeing up a chair.</li>
</ul>

<p>Return the <strong>minimum </strong>number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially <strong>empty</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;EEEEEEE&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;ELELEEL&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second.</p>
</div>

<table>
	<tbody>
		<tr>
			<th>Second</th>
			<th>Event</th>
			<th>People in the Waiting Room</th>
			<th>Available Chairs</th>
		</tr>
		<tr>
			<td>0</td>
			<td>Enter</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>Leave</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Enter</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Leave</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Enter</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Enter</td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td>6</td>
			<td>Leave</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;ELEELEELLL&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s consider that there are 3 chairs in the waiting room. The table below shows the state of the waiting room at each second.</p>
</div>

<table>
	<tbody>
		<tr>
			<th>Second</th>
			<th>Event</th>
			<th>People in the Waiting Room</th>
			<th>Available Chairs</th>
		</tr>
		<tr>
			<td>0</td>
			<td>Enter</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>1</td>
			<td>Leave</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Enter</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Enter</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Leave</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Enter</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>6</td>
			<td>Enter</td>
			<td>3</td>
			<td>0</td>
		</tr>
		<tr>
			<td>7</td>
			<td>Leave</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>8</td>
			<td>Leave</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>9</td>
			<td>Leave</td>
			<td>0</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>s</code> consists only of the letters <code>&#39;E&#39;</code> and <code>&#39;L&#39;</code>.</li>
	<li><code>s</code> represents a valid sequence of entries and exits.</li>
</ul>

# Approach 
* Iterate from left to right over the string and keep track of the number of people in the waiting room using a variable that you will increment on every occurrence of ‘E’ and decrement on every occurrence of ‘L’.
* The answer is the maximum number of people in the waiting room at any instance.

```ini
1. What’s happening in the waiting room?
	•	You start with no one in the room and no chairs set up.
	•	Each character of the string s represents one second’s “event”:
	•	'E' ⇒ someone Enters the room. They need an empty chair immediately.
	•	'L' ⇒ someone Leaves the room, freeing up one chair.

Your goal is to figure out how many chairs you must have at minimum so that no one ever arrives without an available seat.
```

```ini
At any point in time you have:
	•	occupied = how many people are currently sitting in chairs,
	•	max_chairs = the maximum value that occupied ever reaches.

Whenever someone enters, occupied += 1. Whenever someone leaves, occupied -= 1.
The answer you return is the largest occupied ever got—because that’s how many chairs you needed at the busiest moment.
```

1. create a variable and track the occupied and then store that occupied in a array for each iterationa and then return and maximum values in that array and that is number of chair needed. 

```python
class Solution:
    def minimumChairs(self, s: str) -> int:
        occupied = 0
        chairs = []

        for p in s:
            if p == 'E':
                occupied += 1
            else:
                occupied -= 1
            
            chairs.append(occupied)
        
        return max(chairs)
```

```python
class Solution:
    def minChairs(self, s: str) -> int:
        occupied = 0
        max_chairs = 0

        for event in s:
            if event == 'E':
                occupied += 1
                # update the busiest-point if needed
                max_chairs = max(max_chairs, occupied)
            elif event == 'L':
                occupied -= 1
                # we assume input never makes occupied go negative
        return max_chairs
```
