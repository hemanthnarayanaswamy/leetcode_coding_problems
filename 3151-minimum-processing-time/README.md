<h2><a href="https://leetcode.com/problems/minimum-processing-time">3151. Minimum Processing Time</a></h2><h3>Medium</h3><hr><p>You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.</p>

<p>You are given an array <code>processorTime</code> representing the time each processor becomes available and an array <code>tasks</code> representing how long each task takes to complete. Return the&nbsp;<em>minimum</em> time needed to complete all tasks.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>Assign the tasks at indices 4, 5, 6, 7 to the first processor which becomes available at <code>time = 8</code>, and the tasks at indices 0, 1, 2, 3 to the second processor which becomes available at <code>time = 10</code>.&nbsp;</p>

<p>The time taken by the first processor to finish the execution of all tasks is&nbsp;<code>max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16</code>.</p>

<p>The time taken by the second processor to finish the execution of all tasks is&nbsp;<code>max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">23</span></p>

<p><strong>Explanation:</strong></p>

<p>Assign the tasks at indices 1, 4, 5, 6 to the first processor and the others to the second processor.</p>

<p>The time taken by the first processor to finish the execution of all tasks is <code>max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18</code>.</p>

<p>The time taken by the second processor to finish the execution of all tasks is <code>max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == processorTime.length &lt;= 25000</code></li>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= processorTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>tasks.length == 4 * n</code></li>
</ul>

# Approach 
* The problem involves distributing a set of tasks with known processing times to a set of processors with known processing capabilities. The goal is to minimize the total processing time by assigning tasks to processors in an optimal way. This is a scheduling problem where you want to allocate tasks to processors to minimize the overall completion time.

```ini 
Sort the processorTimes array in ascending order. This step ensures that tasks are assigned to processors with the shortest processing times first.

Sort the taskTimes array in descending order. This step sorts the tasks in such a way that the longest tasks are considered first when assigning them to processors.

Initialize processorIndex to 0 and answer to 0. processorIndex keeps track of the current processor being assigned tasks, and answer keeps track of the minimum total processing time.
```
```python
class Solution:
    def minProcessingTime(self, processorTimes, taskTimes):
        processorTimes.sort()
        taskTimes.sort(reverse=True)
        processorIndex = 0
        answer = 0

        for processingTime in processorTimes:
            currentMax = 0
            taskCount = 0

            while processorIndex < len(taskTimes) and taskCount < 4:
                currentMax = max(currentMax, processingTime + taskTimes[processorIndex])
                processorIndex += 1
                taskCount += 1

            answer = max(answer, currentMax)

        return answer
```
---
# Improved Solution 
* For a processing time we only need to find the max for the first element in the tasks for group 4 because that will procude the max result out of other three, so no need to do the calculation for others.  

```python
class Solution:
    def minProcessingTime(self, processorTimes, taskTimes):
        processorTimes.sort()
        taskTimes.sort(reverse=True)
        answer = 0

        for i in range(len(processorTimes)):
            val = processorTimes[i] + taskTimes[i*4]
            if val > answer:
                answer = val
        
        return answer
```
