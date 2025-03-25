<h2><a href="https://leetcode.com/problems/count-days-without-meetings">3430. Count Days Without Meetings</a></h2><h3>Medium</h3><hr><p>You are given a positive integer <code>days</code> representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array <code>meetings</code> of size <code>n</code> where, <code>meetings[i] = [start_i, end_i]</code> represents the starting and ending days of meeting <code>i</code> (inclusive).</p>

<p>Return the count of days when the employee is available for work but no meetings are scheduled.</p>

<p><strong>Note: </strong>The meetings may overlap.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">days = 10, meetings = [[5,7],[1,3],[9,10]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no meeting scheduled on the 4<sup>th</sup> and 8<sup>th</sup> days.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">days = 5, meetings = [[2,4],[1,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no meeting scheduled on the 5<sup>th </sup>day.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">days = 6, meetings = [[1,6]]</span></p>

<p><strong>Output:</strong> 0</p>

<p><strong>Explanation:</strong></p>

<p>Meetings are scheduled for all working days.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= days &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 2</code></li>
	<li><code><font face="monospace">1 &lt;= meetings[i][0] &lt;= meetings[i][1] &lt;= days</font></code></li>
</ul>

# Solution Approach
1. Use Sorting on meetings to process them in order.
2. Use a variable nextAvailableDay (initialized to 1) to track the next day that hasn't been occupied by a meeting. If there is a gap between the nextAvailableDay and the current meeting’s start, count those days as unvisited. After processing a meeting, update nextAvailableDay to meetingEnd + 1.
3. After all meetings, there may still be unvisited days at the end. Ensure you add the remaining unvisited days from temp to days using →
unvisitedDays + max(days - nextAvailableDay + 1

```python
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        meetings.sort()     # Sort the Meetings 
        nextMeeting = 0
        for meeting in meetings:
            if nextMeeting < meeting[0]:
                count += (meeting[0] - nextMeeting) - 1
                nextMeeting = meeting[1]
            elif nextMeeting >= meeting[0]:
                if nextMeeting >= meeting[1]:
                    continue
                else:
                    nextMeeting = meeting[1]

        if nextMeeting < days:
            count += (days - nextMeeting)

        return count
```

## Improved Solution 
* checking if `nextMeeting` if less then the `startmeeting` if True we compute the differencee for the number of free days and change the nextmeeting to the end of meeting time. 
* then if the `nextMeeting` is greater then `start and end` time we skip it as the slot is already occupied and then 
* At the end we check the nextMeeting and working end day to see if they are any unoccupied days. 

```python
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        meetings.sort()
        nextMeeting = 0
        for meeting in meetings:
            startMeet, endMeet = meeting[0], meeting[1]
            if nextMeeting < startMeet:
                count += (startMeet - nextMeeting) - 1
            elif nextMeeting >= startMeet and nextMeeting >= endMeet:
                    continue
            
            nextMeeting = endMeet

        if nextMeeting < days:
            count += (days - nextMeeting)

        return count
```

## Optimal Solution
* `meetings.sort(key=lambda x: x[0])` use sort effectively 
```python
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        meetings.sort(key=lambda x: x[0])
        nextMeeting = 0 
        for meeting in meetings:
            startMeet, endMeet = meeting[0], meeting[1]
            if nextMeeting < startMeet:
                count += (startMeet - nextMeeting) - 1
            elif nextMeeting >= startMeet and nextMeeting >= endMeet:
                    continue
            
            nextMeeting = endMeet

        if nextMeeting < days:
            count += (days - nextMeeting)

        return count
```
