<h2><a href="https://leetcode.com/problems/eliminate-maximum-number-of-monsters">2049. Eliminate Maximum Number of Monsters</a></h2><h3>Medium</h3><hr><p>You are playing a video game where you are defending your city from a group of <code>n</code> monsters. You are given a <strong>0-indexed</strong> integer array <code>dist</code> of size <code>n</code>, where <code>dist[i]</code> is the <strong>initial distance</strong> in kilometers of the <code>i<sup>th</sup></code> monster from the city.</p>

<p>The monsters walk toward the city at a <strong>constant</strong> speed. The speed of each monster is given to you in an integer array <code>speed</code> of size <code>n</code>, where <code>speed[i]</code> is the speed of the <code>i<sup>th</sup></code> monster in kilometers per minute.</p>

<p>You have a weapon that, once fully charged, can eliminate a <strong>single</strong> monster. However, the weapon takes <strong>one minute</strong> to charge. The weapon is fully charged at the very start.</p>

<p>You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a <strong>loss</strong>, and the game ends before you can use your weapon.</p>

<p>Return <em>the <strong>maximum</strong> number of monsters that you can eliminate before you lose, or </em><code>n</code><em> if you can eliminate all the monsters before they reach the city.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dist = [1,3,4], speed = [1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the third monster.
All 3 monsters can be eliminated.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dist = [1,1,2,3], speed = [1,1,1,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> dist = [3,2,4], speed = [5,3,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == dist.length == speed.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= dist[i], speed[i] &lt;= 10<sup>5</sup></code></li>
</ul>

## Solution Approach 
* First we calculate the time using distance and speed then sort that in-order when the mosters will arrive. 
* Initially weapon is fully changed so always the first monster is eliminated `n=1`
* We use a `weapon` variable where `weapon%2 == 0` means weapon is not charged other case its charged. 
* We do a for loop `for i in range(1, len(time_taken)):` from the second monster as first is always eliminated. 
* If `time[i]` is less than one and the weapon is not charged return
* else the monster is eliminated and `n+=1` and every iteration increment weapon.
```python
#### WRONG SOLUTION ####
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_taken = sorted([dist[i]/speed[i] for i in range(len(dist))])
        n = 1
        weapon = 0   #Assume even is not changed, odd is charged
        for i in range(1, len(time_taken)):
            if time_taken[i] - 1 < 1 and weapon%2 == 0:
                return n 
            else:
                n += 1
            weapon += 1

        return n
```
* Not covering all the edge cases 
* `weapon` not required as we can use the index `i` to track the time 
```python
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_taken = sorted([dist[i]/speed[i] for i in range(len(dist))])
        # time_taken = sorted([d/s for d, s in zip(dist, speed)])
        
        for i in range(len(time_taken)):
            if time_taken[i] <= i:  # We check if the monster reaches before we shoot 
                return i
        return len(time_taken)
```

