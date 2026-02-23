<h2><a href="https://leetcode.com/problems/button-with-longest-push-time">3632. Button with Longest Push Time</a></h2><h3>Easy</h3><hr><p>You are given a 2D array <code>events</code> which represents a sequence of events where a child pushes a series of buttons on a keyboard.</p>

<p>Each <code>events[i] = [index<sub>i</sub>, time<sub>i</sub>]</code> indicates that the button at index <code>index<sub>i</sub></code> was pressed at time <code>time<sub>i</sub></code>.</p>

<ul>
	<li>The array is <strong>sorted</strong> in increasing order of <code>time</code>.</li>
	<li>The time taken to press a button is the difference in time between consecutive button presses. The time for the first button is simply the time at which it was pressed.</li>
</ul>

<p>Return the <code>index</code> of the button that took the <strong>longest</strong> time to push. If multiple buttons have the same longest time, return the button with the <strong>smallest</strong> <code>index</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">events = [[1,2],[2,5],[3,9],[1,15]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Button with index 1 is pressed at time 2.</li>
	<li>Button with index 2 is pressed at time 5, so it took <code>5 - 2 = 3</code> units of time.</li>
	<li>Button with index 3 is pressed at time 9, so it took <code>9 - 5 = 4</code> units of time.</li>
	<li>Button with index 1 is pressed again at time 15, so it took <code>15 - 9 = 6</code> units of time.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">events = [[10,5],[1,7]]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Button with index 10 is pressed at time 5.</li>
	<li>Button with index 1 is pressed at time 7, so it took <code>7 - 5 = 2</code> units of time.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= events.length &lt;= 1000</code></li>
	<li><code>events[i] == [index<sub>i</sub>, time<sub>i</sub>]</code></li>
	<li><code>1 &lt;= index<sub>i</sub>, time<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li>The input is generated such that <code>events</code> is sorted in increasing order of <code>time<sub>i</sub></code>.</li>
</ul>

# Solution
* I used a simple iterative approach to solve this problem. I initialized two variables, `longestTime` and `res`, to keep track of the `maximum time difference` and the `index` of the corresponding button which is initiallzes to first event by  default. 
* Then, I iterated through the list of events, calculating the time difference between each pair of consecutive events. using `prevTime` by changing it to current as we move. 
*  If the time difference was greater than or equal to the current maximum time difference, I updated current_total and current_index accordingly.


```python
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        prevTime = longestTime = events[0][1]
        res = events[0][0]

        for i in range(1, len(events)):
            idx, time = events[i]
            tmpTime = (time - prevTime)

            if tmpTime > longestTime:
                longestTime = tmpTime
                res = idx
            elif tmpTime == longestTime:
                res = min(res, idx)
            
            prevTime = time
        
        return res
```
