<h2><a href="https://leetcode.com/problems/car-fleet">883. Car Fleet</a></h2><h3>Medium</h3><hr><p>There are <code>n</code> cars at given miles away from the starting mile 0, traveling to reach the mile <code>target</code>.</p>

<p>You are given two integer arrays&nbsp;<code>position</code> and <code>speed</code>, both of length <code>n</code>, where <code>position[i]</code> is the starting mile of the <code>i<sup>th</sup></code> car and <code>speed[i]</code> is the speed of the <code>i<sup>th</sup></code> car in miles per hour.</p>

<p>A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.</p>

<p>A <strong>car fleet</strong> is a single car or a group of cars driving next to each other. The speed of the car fleet is the <strong>minimum</strong> speed of any car in the fleet.</p>

<p>If a car catches up to a car fleet at the mile <code>target</code>, it will still be considered as part of the car fleet.</p>

<p>Return the number of car fleets that will arrive at the destination.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at <code>target</code>.</li>
	<li>The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.</li>
	<li>The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches <code>target</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = 10, position = [3], speed = [3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>
There is only one car, hence there is only one fleet.</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = 100, position = [0,2,4], speed = [4,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.</li>
	<li>Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches <code>target</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == position.length == speed.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt; target &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= position[i] &lt; target</code></li>
	<li>All the values of <code>position</code> are <strong>unique</strong>.</li>
	<li><code>0 &lt; speed[i] &lt;= 10<sup>6</sup></code></li>
</ul>

# Intuition
Call the "lead fleet" the fleet furthest in position.

- If the car `S` (Second) behind the lead car `F` (First) would **arrive earlier**, then `S` forms a fleet with the lead car `F`. 
- Otherwise, fleet `F` is final as no car can catch up to it - cars behind `S` would form fleets with `S`, never `F`.

### Algorithm

- A car is a `(position, speed)` which implies some arrival time `(target - position) / speed`. **Sort the cars by position.**
- Now apply the above reasoning -` if the lead fleet drives away, then count it and continue. Otherwise, merge the fleets and continue.`
# Approach
* We `sort()`, the positions based on which cars are closer to the target, by mapping it with the speeds. 
```python
order = [(p,s) for p,s in zip(position, speed)]
order.sort(reverse=True)
```
* Now for each car, we calculate the `time`, it'll take to reach the `target`, and append it into the `stack`.
* This is where we need to check for the `fleets` condition. 

```ini
Lets say we have time x, in the stack

the next car time is faster x-1, that means this next car will catch up to the previous car before reaching the destination

As per the question, when this next car reaches the previous car, the next car slows down and travels with the previous car to reach the target. 

That means, the take to this car will also become same as the time in stack (So no need to append a new time in stack)

Now lets say other car which is slower then the previous car, this car will never catch up to the car in front of it and it alone with be the fleet so we append its time to the stack.

At the end stack will have all the car fleets time, so the length of stack will be the number of car fleets.
```
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = [(p,s) for p,s in zip(position, speed)]
        order.sort(reverse=True)
        stack = []

        for p,s in order:
            t = (target - p)/s # Don't round off time value 
            if stack:
                if t > stack[-1]:  # We only add time to stack, if the car will not catch up to the previous car for which time should be less then previous
                    stack.append(t) 
            else:
                stack.append(t)
        
        return len(stack)
```
---
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = sorted(zip(position, speed), reverse=True)
        stack = []

        for p,s in order:
            t = (target - p)/s

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
```
