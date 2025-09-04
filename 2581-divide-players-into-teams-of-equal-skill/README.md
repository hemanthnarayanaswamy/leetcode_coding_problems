<h2><a href="https://leetcode.com/problems/divide-players-into-teams-of-equal-skill">2581. Divide Players Into Teams of Equal Skill</a></h2><h3>Medium</h3><hr><p>You are given a positive integer array <code>skill</code> of <strong>even</strong> length <code>n</code> where <code>skill[i]</code> denotes the skill of the <code>i<sup>th</sup></code> player. Divide the players into <code>n / 2</code> teams of size <code>2</code> such that the total skill of each team is <strong>equal</strong>.</p>

<p>The <strong>chemistry</strong> of a team is equal to the <strong>product</strong> of the skills of the players on that team.</p>

<p>Return <em>the sum of the <strong>chemistry</strong> of all the teams, or return </em><code>-1</code><em> if there is no way to divide the players into teams such that the total skill of each team is equal.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> skill = [3,2,5,1,3,4]
<strong>Output:</strong> 22
<strong>Explanation:</strong> 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> skill = [3,4]
<strong>Output:</strong> 12
<strong>Explanation:</strong> 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> skill = [1,1,2,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 
There is no way to divide the players into teams such that the total skill of each team is equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= skill.length &lt;= 10<sup>5</sup></code></li>
	<li><code>skill.length</code> is even.</li>
	<li><code>1 &lt;= skill[i] &lt;= 1000</code></li>
</ul>

# Solution 
```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        target = 0
        result = 0
        
        l, r = 0, len(skill)-1

        while l < r:
            a, b = skill[l], skill[r]
            if target and a+b != target:
                    return -1
            else:
                target = a + b
            result += (a*b)
            l += 1
            r -= 1
        
        return result
```
---
# Sorting Approach 
* Sort the input array `skill` in ascending order.
* Initialize:
     * a variable `n` to the length of the `skill` array.
     * a variable `totalChemistry` to 0, which will store the sum of all team chemistries.
* Calculate the `targetTeamSkill` by adding the first and last elements of the sorted array.
* Iterate through the first half of the array:
* 	Calculate `currentTeamSkill` by adding the `i-th` element from the start and the `i-th` element from the end.
			* If `currentTeamSkill` doesn't match `targetTeamSkill`, return `-1`.
			* Calculate the chemistry of the current team by multiplying the skills of the two team members.
			* Add the calculated chemistry to `totalChemistry`.
* Return `totalChemistry` as the answer.

```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        total_chemistry = 0
        target_team_skill = skill[0] + skill[-1]

        for i in range(n // 2):
            left, right = skill[i], skill[n - 1 - i]

            if left + right != target_team_skill:
                return -1
            
            total_chemistry += (left * right)
        
        return total_chemistry
```
---
# Frequency Table Approach
* Create a hash map `skillMap` to store the frequency of each skill value. 
* Here The `totalSum` should be made into pairs, check if the pairing is possible or not initially. 
```python
totalSum = sum(skill)

if totalSum %( n // 2):
    return -1 
# The total Sum should be split into pairs that is half the length of array if not return 
```
* To calculate the target sum for each pair divide the total sum into each pair to find the sum of each pair. 
```python
total = sum(skill)
target = total // (n // 2)  # Each pair should sum to this
```

```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)

        # Check if total skill can be evenly distributed
        if total_skill % (n // 2) != 0:
            return -1

        target_skill = total_skill // (n // 2)
        skill_map = Counter(skill)
        total_chemistry = 0

        # Iterate through unique skill values
        for curr_skill, curr_freq in skill_map.items():
            partner_skill = target_skill - curr_skill

            # Check if valid partner skill exists with matching frequency
            if (
                partner_skill not in skill_map
                or curr_freq != skill_map[partner_skill]
            ):
                return -1

            # Calculate chemistry for all pairs with this skill
            total_chemistry += curr_skill * partner_skill * curr_freq

        # Return half of total chemistry (as each pair is counted twice)
        return total_chemistry // 2
```
---
```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        count = Counter(skill)

        if total % (len(skill) // 2) != 0:
            return -1
        
        avg = total // (len(skill) // 2)
        res = 0

        for s, c in count.items():
            partner = avg - s
            if partner not in count or count[partner] != c:
                return -1
            res += s * partner * c
            
        return res // 2
```
