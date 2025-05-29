<h2><a href="https://leetcode.com/problems/count-of-matches-in-tournament">1806. Count of Matches in Tournament</a></h2><h3>Easy</h3><hr><p>You are given an integer <code>n</code>, the number of teams in a tournament that has strange rules:</p>

<ul>
	<li>If the current number of teams is <strong>even</strong>, each team gets paired with another team. A total of <code>n / 2</code> matches are played, and <code>n / 2</code> teams advance to the next round.</li>
	<li>If the current number of teams is <strong>odd</strong>, one team randomly advances in the tournament, and the rest gets paired. A total of <code>(n - 1) / 2</code> matches are played, and <code>(n - 1) / 2 + 1</code> teams advance to the next round.</li>
</ul>

<p>Return <em>the number of matches played in the tournament until a winner is decided.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 6
<strong>Explanation:</strong> Details of the tournament: 
- 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
- 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 3 + 2 + 1 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 14
<strong>Output:</strong> 13
<strong>Explanation:</strong> Details of the tournament:
- 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
- 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
- 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
- 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
Total number of matches = 7 + 3 + 2 + 1 = 13.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 200</code></li>
</ul>

# Solution 
* Just following the porvided conditions 

```python
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while n > 1:
            advanceTeam = 0
            if n % 2 == 0:
                advanceTeam = n // 2
                n = advanceTeam
            else:
                advanceTeam = (n-1) // 2
                n = advanceTeam + 1
            
            matches += advanceTeam
        
        return matches
```

# Optimal Solution 
```python
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res, teams = 0, n
        while teams > 1:
            res += teams // 2
            teams = teams // 2 + teams % 2

        return res
```

```bash
Instead of simulating the entire tournament, here we will directly consider the beginning and end of the tournament.

In this tournament, when a team loses, they are eliminated and will no longer play any matches.

There are n teams, and 1 winner. Thus, n - 1 teams will be eliminated.

Each match is played between two teams. One team wins, one team loses. Thus, each match eliminates exactly one team.

As n - 1 teams will be eliminated, there will be n - 1 matches played, with each match eliminating a team.
```

```python
class Solution:
    def numberOfMatches(self, num: int) -> int:
        return num - 1
```
