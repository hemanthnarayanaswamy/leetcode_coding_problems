<h2><a href="https://leetcode.com/problems/most-visited-sector-in-a-circular-track">1682. Most Visited Sector in  a Circular Track</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code> and an integer array <code>rounds</code>. We have a circular track which consists of <code>n</code> sectors labeled from <code>1</code> to <code>n</code>. A marathon will be held on this track, the marathon consists of <code>m</code> rounds. The <code>i<sup>th</sup></code> round starts at sector <code>rounds[i - 1]</code> and ends at sector <code>rounds[i]</code>. For example, round 1 starts at sector <code>rounds[0]</code> and ends at sector <code>rounds[1]</code></p>

<p>Return <em>an array of the most visited sectors</em> sorted in <strong>ascending</strong> order.</p>

<p>Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/14/tmp.jpg" style="width: 433px; height: 341px;" />
<pre>
<strong>Input:</strong> n = 4, rounds = [1,3,1,2]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --&gt; 2 --&gt; 3 (end of round 1) --&gt; 4 --&gt; 1 (end of round 2) --&gt; 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, rounds = [2,1,2,1,2,1,2,1,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 7, rounds = [1,3,5,7]
<strong>Output:</strong> [1,2,3,4,5,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= m &lt;= 100</code></li>
	<li><code>rounds.length == m + 1</code></li>
	<li><code>1 &lt;= rounds[i] &lt;= n</code></li>
	<li><code>rounds[i] != rounds[i + 1]</code> for <code>0 &lt;= i &lt; m</code></li>
</ul>

# Solution 
```python
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        trackVisit = [0] * n
        start = rounds[0]
        i = 1

        while i < len(rounds):
            end = rounds[i]
            if end < start:
                end += n

            for j in range(start-1, end):
                trackVisit[j%n] += 1
            start = (rounds[i] + 1) % n
            i += 1
        
        maxVisits = max(trackVisit)

        return [i+1 for i in range(len(trackVisit)) if trackVisit[i] == maxVisits]
```
---
```python
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # counter of each sector
        counter = [0] * (n + 1)
        
        # simulate circulating the track
        start = rounds[0]
        counter[start] += 1
        
        for i in range(1, len(rounds)):
            end = rounds[i]
            
            while start != end:
                start = start % n + 1
                counter[start] += 1
                
            start = end
        
        # find the largest visted counter
        most = max(counter)
        
        result = []
        
        # output sector with most visited in ascending order
        for i in range(1, len(counter)):
            if counter[i] == most:
                result.append(i)
        
        return result
```

A marathon is ran around a circular track (potentially several times around). The circular track is divided into n sectors, starting from sector 1 in increasing order to sector n. The marathon consists of m stops, where each stop falls within a sector, and the last stop marks the end of the marathon. Given n, and stops, find the sectors which are visited the most through the entire marathon.

A sector is considered visited both when a racer runs through it, as well as when a racer starts or stops in that sector. That sector can be visited again after the runner leaves the sector and comes back around to it.

**In the next race, start point is considered from where the previous race ended, and since that stop was counted in the previous race, so in the new race that stop is not counted as visited because we are restarting from that point on wards**

```ini
To resolve the circular problem, if the end < start, that means we have run the circle, so make it start, end+n
```

# Optimal Solution
1. The round list contains the sectors where the rounds start and end. 
     * The first element `rounds[0]` indicated where the first round begins, and the last element `rounds[-1]` indicates where the last round ends.
2. If the `starting sector <= the ending sector`, it means that the marathon does not wrap around the circular track. 
     * In this case, all sectors from `start_sector` to `end_sector` are visited. 
 3. If the `starting sector > ending sector`, it indicates that the marathon wraps around. 
     * In this case, all sectors from `1 to end_sector` are **visited**, and then all sectors from `start_sector` to `n` are visited. 
     * For example, if the rounds start at `sector 3` and end at `sector 1`, on the track with 4 sectors, the sectors visited will include both sectors at the beginning of the track and those at the end.
     
```ini
list(range(1, end_sector + 1): This represents the sectors that are visited before the marathon wraps back around to the starting sector. 
list(range(start_sector, n+1): This represents the sectors that are visited after the marathon wraps around. 
```

```ini
Explanation:
if n = 4, rounds = [1,3,1,2]
than [1,2,3,4,1,2]
output is [1,2]

if n = 3 rounds = [3,1,2,3,1]
than [3,1,2,3,1]
output is [1,3]

if n = 4 rounds = [1,4,2,3]
than [1,2,3,4,1,2,3]
output is [1,2,3]

which means all steps moved in the middle will happen again and again and again, so they are useless.
The only important things are start point and end point.
```
---
1. If `start <= end`, that means we have run in the order and did not do a circular path and hence the most visited sectors will be the once in-between inclusive of `start to end`.
2. Now is `start > end`, that means: the most visited sectors are 
    `1 to end` and `start to n` 
```python
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]

        if start <= end:
            return [i for i in range(start, end+1)]
        
        res = []

        for i in range(1, end+1):
            res.append(i)

        for j in range(start, n+1):
            res.append(j)
        
        return res
```
---
```python
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[len(rounds) - 1] 
        r = []
        if s <= e:
            for i in range(s, e+1): r.append(i)
        else:
            for i in range(1, e+1): r.append(i)
            for i in range(s, n+1): r.append(i)
        return r
```
