<h2><a href="https://leetcode.com/problems/determine-the-winner-of-a-bowling-game">2684. Determine the Winner of a Bowling Game</a></h2><h3>Easy</h3><hr><p>You are given two <strong>0-indexed</strong> integer arrays <code><font face="monospace">player1</font></code> and <code>player2</code>, representing the number of pins that player 1 and player 2 hit in a bowling game, respectively.</p>

<p>The bowling game consists of <code>n</code> turns, and the number of pins in each turn is exactly 10.</p>

<p>Assume a player hits <code>x<sub>i</sub></code> pins in the i<sup>th</sup> turn. The value of the i<sup>th</sup> turn for the player is:</p>

<ul>
	<li><code>2x<sub>i</sub></code> if the player hits 10 pins <b>in either (i - 1)<sup>th</sup> or (i - 2)<sup>th</sup> turn</b>.</li>
	<li>Otherwise, it is <code>x<sub>i</sub></code>.</li>
</ul>

<p>The <strong>score</strong> of the player is the sum of the values of their <code>n</code> turns.</p>

<p>Return</p>

<ul>
	<li>1 if the score of player 1 is more than the score of player 2,</li>
	<li>2 if the score of player 2 is more than the score of player 1, and</li>
	<li>0 in case of a draw.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">player1 = [5,10,3,2], player2 = [6,5,7,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.</p>

<p>The score of player 2 is 6 + 5 + 7 + 3 = 21.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">player1 = [3,5,7,6], player2 = [8,10,10,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The score of player 1 is 3 + 5 + 7 + 6 = 21.</p>

<p>The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">player1 = [2,3], player2 = [4,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The score of player1 is 2 + 3 = 5.</p>

<p>The score of player2 is 4 + 1 = 5.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.</p>

<p>The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == player1.length == player2.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= player1[i], player2[i] &lt;= 10</code></li>
</ul>

# Solution 
```python
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        i = 0
        s1 = s2 = 0
        p1_multiplier = 0
        p2_multiplier = 0

        while i < len(player1):
            p1 = player1[i]
            p2 = player2[i]

            if p1_multiplier:
                s1 += player1[i]*2
                p1_multiplier -= 1
            else:
                s1 += player1[i]
            
            if p2_multiplier:
                s2 += player2[i]*2
                p2_multiplier -= 1
            else:
                s2 += player2[i]

            if p1 == 10:
                p1_multiplier = 2
            if p2 == 10:
                p2_multiplier = 2
            
            i += 1
        
        if s1 > s2: return 1
        if s1 < s2: return 2
        return 0
```
# Optimal Solution
```python
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(arr):
            tot = 0
            prev = 0
            prev2 = 0
            for v in arr:
                if prev == 10 or prev2 == 10:
                    tot += 2 * v
                else:
                    tot += v
                prev2 = prev
                prev = v
            return tot

        s1 = score(player1)
        s2 = score(player2)
        if s1 > s2: return 1
        if s1 < s2: return 2
        return 0
```
