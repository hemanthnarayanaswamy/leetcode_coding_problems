<h2><a href="https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage">2471. Minimum Amount of Time to Collect Garbage</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array of strings <code>garbage</code> where <code>garbage[i]</code> represents the assortment of garbage at the <code>i<sup>th</sup></code> house. <code>garbage[i]</code> consists only of the characters <code>&#39;M&#39;</code>, <code>&#39;P&#39;</code> and <code>&#39;G&#39;</code> representing one unit of metal, paper and glass garbage respectively. Picking up <strong>one</strong> unit of any type of garbage takes <code>1</code> minute.</p>

<p>You are also given a <strong>0-indexed</strong> integer array <code>travel</code> where <code>travel[i]</code> is the number of minutes needed to go from house <code>i</code> to house <code>i + 1</code>.</p>

<p>There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house <code>0</code> and must visit each house <strong>in order</strong>; however, they do <strong>not</strong> need to visit every house.</p>

<p>Only <strong>one</strong> garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks <strong>cannot</strong> do anything.</p>

<p>Return<em> the <strong>minimum</strong> number of minutes needed to pick up all the garbage.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> garbage = [&quot;G&quot;,&quot;P&quot;,&quot;GP&quot;,&quot;GG&quot;], travel = [2,4,3]
<strong>Output:</strong> 21
<strong>Explanation:</strong>
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> garbage = [&quot;MMM&quot;,&quot;PGM&quot;,&quot;GP&quot;], travel = [3,10]
<strong>Output:</strong> 37
<strong>Explanation:</strong>
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= garbage.length &lt;= 10<sup>5</sup></code></li>
	<li><code>garbage[i]</code> consists of only the letters <code>&#39;M&#39;</code>, <code>&#39;P&#39;</code>, and <code>&#39;G&#39;</code>.</li>
	<li><code>1 &lt;= garbage[i].length &lt;= 10</code></li>
	<li><code>travel.length == garbage.length - 1</code></li>
	<li><code>1 &lt;= travel[i] &lt;= 100</code></li>
</ul>

# Solution Approach
* We calculate the prefix of the time travelled.
```
travel_prefix = [0]

    for time in travel:
        travel_prefix.append(travel_prefix[-1]+time)
```
* And Keep the Count of all the types of grabages.
```
overall_garbage = ''.join(garbage)
    t_m = overall_garbage.count('M')
    t_p = overall_garbage.count('P')
    t_g = overall_garbage.count('G')
```
* Now we do 3 seperate iterations from the end of the array
* If any type of garbage is detected at any position then we compute the time as ```count of Grabage + Prefix Time required to travel to that Position```

```python
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel_prefix = [0]

        for time in travel:
            travel_prefix.append(travel_prefix[-1]+time)
        
        overall_garbage = ''.join(garbage)
        t_m = overall_garbage.count('M')
        t_p = overall_garbage.count('P')
        t_g = overall_garbage.count('G')

        for i in range(len(garbage)-1, -1, -1):
            if 'M' in garbage[i]:
                t_m += travel_prefix[i]
                break

        for i in range(len(garbage)-1, -1, -1):
            if 'P' in garbage[i]:
                t_p += travel_prefix[i]
                break

        for i in range(len(garbage)-1, -1, -1):
            if 'G' in garbage[i]:
                t_g += travel_prefix[i]
                break

        return t_m + t_p + t_g
```

## Improved Solution 
```python
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Step 1: Build prefix sum for travel
        n = len(garbage)
        travel_prefix = [0] * n
        for i in range(1, n):
            travel_prefix[i] = travel_prefix[i-1] + travel[i-1]
        
        total_pickups = {'M': 0, 'P': 0, 'G': 0}
        last_seen = {'M': 0, 'P': 0, 'G': 0}

        # Step 2: Count pickups and record last house for each type
        for i, types_garbage in enumerate(garbage):
            for char in types_garbage:
                total_pickups[char] += 1
                last_seen[char] = i

        # Step 3: Calculate total time
        total_time = 0
        
        for char in ['M', 'P', 'G']:
            if total_pickups[char] > 0:
                total_time += total_pickups[char] + travel_prefix[last_seen[char]]

        return total_time
```

## Optimal Solution 
```python
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Step 1: Build prefix sum for travel
        n = len(garbage)

        travel_prefix = [0] * n
        for i in range(1, n):
            travel_prefix[i] = travel_prefix[i-1] + travel[i-1]
        
        travel_prefix = travel_prefix [::-1]
        garbage = garbage[::-1]

        total_time = 0
        M, P, G = 1, 1, 1

        for i in range(n):
            if "M" in garbage[i] and M:
                total_time += travel_prefix[i]
                M = 0
            if "G" in garbage[i] and G:
                total_time += travel_prefix[i]
                G = 0
            if "P" in garbage[i] and P:
                total_time += travel_prefix[i]
                P = 0

            if not(P) and not(G) and not(M):
                break
        
        total_time += len("".join(garbage))

        return total_time
```
