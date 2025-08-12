<h2><a href="https://leetcode.com/problems/average-waiting-time">1803. Average Waiting Time</a></h2><h3>Medium</h3><hr><p>There is a restaurant with a single chef. You are given an array <code>customers</code>, where <code>customers[i] = [arrival<sub>i</sub>, time<sub>i</sub>]:</code></p>

<ul>
	<li><code>arrival<sub>i</sub></code> is the arrival time of the <code>i<sup>th</sup></code> customer. The arrival times are sorted in <strong>non-decreasing</strong> order.</li>
	<li><code>time<sub>i</sub></code> is the time needed to prepare the order of the <code>i<sup>th</sup></code> customer.</li>
</ul>

<p>When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers <strong>in the order they were given in the input</strong>.</p>

<p>Return <em>the <strong>average</strong> waiting time of all customers</em>. Solutions within <code>10<sup>-5</sup></code> from the actual answer are considered accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> customers = [[1,2],[2,5],[4,3]]
<strong>Output:</strong> 5.00000
<strong>Explanation:
</strong>1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> customers = [[5,2],[5,4],[10,3],[20,1]]
<strong>Output:</strong> 3.25000
<strong>Explanation:
</strong>1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= customers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arrival<sub>i</sub>, time<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>arrival<sub>i&nbsp;</sub>&lt;= arrival<sub>i+1</sub></code></li>
</ul>

# Approach 
1. Initialize integers `nextIdleTime` and `netWaitTime` with 0.
2. Set `nextIdleTime` as the maximum of customer's arrival time and the current value of `nextIdleTime` plus the order preparation time.
3. Increment `netWaitTime` by the difference of `nextIdleTime` and the `customer's arrival time`.
4. Divide the `netWaitTime` by customers.size to get the averageWaitTime.

```python
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0.0
        
        total_waiting_time = 0
        chef_available_time = 0

        for arrival_time, cooking_time in customers:
            # Chef starts cooking after the customer arrives or when chef is avaiable 
						cooking_start_time = max(arrival_time, chef_available_time)
            
						# Food will be ready at when we starts to cook and the cooking time of customer meal
            food_ready_time = cooking_start_time + cooking_time 
           
					 # now total wait time becomes when the food was ready and the time customer arrived
            total_waiting_time += (food_ready_time - arrival_time)
           
					 # chef available time will be when food was ready becasue that is when chef will be free
            chef_available_time = food_ready_time
        
        return total_waiting_time / len(customers)
```

# Optimal Solution 
```python
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_wait = 0
        
        for arrival, duration in customers:
            if current_time < arrival:
                current_time = arrival  
                
            current_time += duration
            total_wait += current_time - arrival  

        return total_wait / len(customers)
```
# Key Insights

* Waiting time = (time when food is ready) - (arrival time)
* The chef might be idle when a customer arrives, or might still be cooking for a previous customer
* If the chef is idle, they start cooking immediately when the customer arrives
* If the chef is busy, the customer waits until the chef finishes the current order

### Step-by-Step Approach
Let's trace through an example:

* Customer 1: arrives at time 1, needs 2 minutes to cook
* Customer 2: arrives at time 2, needs 1 minute to cook
* Customer 3: arrives at time 4, needs 3 minutes to cook


* Customer 1 arrives at t=1, chef starts cooking, finishes at t=3. Wait time = 3-1 = 2
* Customer 2 arrives at t=2, but chef is busy until t=3, so cooking starts at t=3, finishes at t=4. Wait time = 4-2 = 2
* Customer 3 arrives at t=4, chef just finished, starts immediately, finishes at t=7. Wait time = 7-4 = 3
