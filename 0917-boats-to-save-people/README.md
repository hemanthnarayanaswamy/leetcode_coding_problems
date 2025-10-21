<h2><a href="https://leetcode.com/problems/boats-to-save-people">917. Boats to Save People</a></h2><h3>Medium</h3><hr><p>You are given an array <code>people</code> where <code>people[i]</code> is the weight of the <code>i<sup>th</sup></code> person, and an <strong>infinite number of boats</strong> where each boat can carry a maximum weight of <code>limit</code>. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most <code>limit</code>.</p>

<p>Return <em>the minimum number of boats to carry every given person</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> people = [1,2], limit = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 boat (1, 2)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> people = [3,2,2,1], limit = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 boats (1, 2), (2) and (3)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> people = [3,5,3,4], limit = 5
<strong>Output:</strong> 4
<strong>Explanation:</strong> 4 boats (3), (3), (4), (5)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= people[i] &lt;= limit &lt;= 3 * 10<sup>4</sup></code></li>
</ul>

# Solution 
* I need at least n/2 boats for the job, so greedily I will try to fit two people in one boat.
* At the same time I also have to make sure that the total weights of the two people I am pairing up does not exceed limit. So if I pare up minimum and second minimum together, and keep on pairing them up like this, then at some later stage I risk the combined weights of the two people exceeding limit.
* So for this let us remove all the people with `weight >= limit`, as they will take one complete boat. 
* For the remaining ones, `the maximum one of them has to be paired up with someone. So let us try to pair him up with the minimum weighted person`. 
* Now notice that if the maximum guy cannot be paired with the minimum guy then he cannot be paired up with anyone else (I hope that the reader is getting the intuition so as to why we pair max with min).
*  Otherwise we assign one boat to the max guy and proceed like this till everyone has got at least one boat.

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        n = len(people)
        l, r = 0, n-1

        for i in range(n):
            if people[i] >= limit:
                r = i - 1
                break 
        
        boats += len(people[r+1:])
        print()

        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
        
        return boats
```
---
```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        n = len(people)
        l, r = 0, n-1

        for i in range(n):
            if people[i] >= limit:
                r = i - 1
                break 
        # New r idx will be where that person can the paired with min weight person to share a boat
        
        boats += len(people[r+1:]) # Boats for people greater in Weight

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                
            boats += 1
            r -= 1
        
        return boats
```
---
* Drop the first loop. You don’t need to pre-split heavy people; two pointers handle all cases.
* Avoid `len(people[r+1:])`. That slice allocates. Count boats in one pass.
* Core invariant: try to pair the heaviest with the lightest. If they fit, move both. Else send the heaviest alone.
```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            boats += 1
            r -= 1
        if l == r:
            boats += 1
        return boats
```
