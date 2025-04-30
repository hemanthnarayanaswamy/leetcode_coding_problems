<h2><a href="https://leetcode.com/problems/find-players-with-zero-or-one-losses">1354. Find Players With Zero or One Losses</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>matches</code> where <code>matches[i] = [winner<sub>i</sub>, loser<sub>i</sub>]</code> indicates that the player <code>winner<sub>i</sub></code> defeated player <code>loser<sub>i</sub></code> in a match.</p>

<p>Return <em>a list </em><code>answer</code><em> of size </em><code>2</code><em> where:</em></p>

<ul>
	<li><code>answer[0]</code> is a list of all players that have <strong>not</strong> lost any matches.</li>
	<li><code>answer[1]</code> is a list of all players that have lost exactly <strong>one</strong> match.</li>
</ul>

<p>The values in the two lists should be returned in <strong>increasing</strong> order.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>You should only consider the players that have played <strong>at least one</strong> match.</li>
	<li>The testcases will be generated such that <strong>no</strong> two matches will have the <strong>same</strong> outcome.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
<strong>Output:</strong> [[1,2,10],[4,5,7,8]]
<strong>Explanation:</strong>
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matches = [[2,3],[1,3],[5,4],[6,4]]
<strong>Output:</strong> [[1,2,5,6],[]]
<strong>Explanation:</strong>
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= matches.length &lt;= 10<sup>5</sup></code></li>
	<li><code>matches[i].length == 2</code></li>
	<li><code>1 &lt;= winner<sub>i</sub>, loser<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>winner<sub>i</sub> != loser<sub>i</sub></code></li>
	<li>All <code>matches[i]</code> are <strong>unique</strong>.</li>
</ul>

# Solution
* Track the number of losses for each player in the hashmap 
* Then get the result for the noloss and onelos, sort and return the list

```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossTracker = {}
        onelose = []
        nolose = []

        for match in matches:
            w, l = match[0], match[1]
            lossTracker[l] = lossTracker.get(l, 0) + 1
            if w not in lossTracker:
                lossTracker[w] = 0

        
        #lossTrackerSort = dict(sorted(lossTracker.items(), key=lambda item: item[0]))
        
        for player, lose in lossTracker.items():
            if lose == 0:
                nolose.append(player)
            
            elif lose == 1:
                onelose.append(player)

        nolose.sort()
        onelose.sort()

        return [nolose, onelose]
```

## Improved Solution
```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossTracker = {}
        onelose = []
        nolose = []

        # for match in matches:
        #     w, l = match[0], match[1]
        #     lossTracker[l] = lossTracker.get(l, 0) + 1
        #     if w not in lossTracker:
        #         lossTracker[w] = 0
        for w, l in matches:
            lossTracker[l] = lossTracker.get(l, 0) + 1
            if w not in lossTracker:
                lossTracker[w] = 0
        
        #lossTrackerSort = dict(sorted(lossTracker.items(), key=lambda item: item[0]))
        
        for player, lose in lossTracker.items():
            if lose == 0:
                nolose.append(player)
            
            elif lose == 1:
                onelose.append(player)

        return [sorted(nolose), sorted(onelose)]
```

## Optimal Solution
```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_losses, one_loss, more_losses = set(), set(), set()

        for w, l in matches:
            # ensure winners with no losses so far
            if w not in one_loss and w not in more_losses:
                zero_losses.add(w)

            # process this loss
            if l in zero_losses:
                zero_losses.remove(l)
                one_loss.add(l)
            elif l in one_loss:
                one_loss.remove(l)
                more_losses.add(l)
            elif l not in more_losses:
                # first-ever loss
                one_loss.add(l)
            # else: l is already in more_losses, do nothing

        return [
            sorted(zero_losses),
            sorted(one_loss)
        ]
```
