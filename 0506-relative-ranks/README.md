<h2><a href="https://leetcode.com/problems/relative-ranks">506. Relative Ranks</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>score</code> of size <code>n</code>, where <code>score[i]</code> is the score of the <code>i<sup>th</sup></code> athlete in a competition. All the scores are guaranteed to be <strong>unique</strong>.</p>

<p>The athletes are <strong>placed</strong> based on their scores, where the <code>1<sup>st</sup></code> place athlete has the highest score, the <code>2<sup>nd</sup></code> place athlete has the <code>2<sup>nd</sup></code> highest score, and so on. The placement of each athlete determines their rank:</p>

<ul>
	<li>The <code>1<sup>st</sup></code> place athlete&#39;s rank is <code>&quot;Gold Medal&quot;</code>.</li>
	<li>The <code>2<sup>nd</sup></code> place athlete&#39;s rank is <code>&quot;Silver Medal&quot;</code>.</li>
	<li>The <code>3<sup>rd</sup></code> place athlete&#39;s rank is <code>&quot;Bronze Medal&quot;</code>.</li>
	<li>For the <code>4<sup>th</sup></code> place to the <code>n<sup>th</sup></code> place athlete, their rank is their placement number (i.e., the <code>x<sup>th</sup></code> place athlete&#39;s rank is <code>&quot;x&quot;</code>).</li>
</ul>

<p>Return an array <code>answer</code> of size <code>n</code> where <code>answer[i]</code> is the <strong>rank</strong> of the <code>i<sup>th</sup></code> athlete.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> score = [5,4,3,2,1]
<strong>Output:</strong> [&quot;Gold Medal&quot;,&quot;Silver Medal&quot;,&quot;Bronze Medal&quot;,&quot;4&quot;,&quot;5&quot;]
<strong>Explanation:</strong> The placements are [1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, 5<sup>th</sup>].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> score = [10,3,8,9,4]
<strong>Output:</strong> [&quot;Gold Medal&quot;,&quot;5&quot;,&quot;Bronze Medal&quot;,&quot;Silver Medal&quot;,&quot;4&quot;]
<strong>Explanation:</strong> The placements are [1<sup>st</sup>, 5<sup>th</sup>, 3<sup>rd</sup>, 2<sup>nd</sup>, 4<sup>th</sup>].

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == score.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= score[i] &lt;= 10<sup>6</sup></code></li>
	<li>All the values in <code>score</code> are <strong>unique</strong>.</li>
</ul>

# Solution 
* Sort and map the index into the actual number 
* Then do the actual implementation of the score and check conditions for gold, silver and bronze.

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreRank = {s: str(i+1) for i, s in enumerate(sorted(score, reverse=True))}

        rank = []

        for s in score:
            if scoreRank[s] == '1':
                rank.append("Gold Medal")
            elif scoreRank[s] == '2':
                rank.append("Silver Medal")
            elif scoreRank[s] == '3':
                rank.append("Bronze Medal")
            else:
                rank.append(scoreRank[s])
        
        return rank
```

# Optimal Solution 
```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_to_idx = {}
        for i in range(len(score)):
            score_to_idx[score[i]] = i

        score.sort(reverse=True)
        ans = [0]*len(score)
        ans[score_to_idx[score[0]]] = "Gold Medal"
        if len(score) > 1: ans[score_to_idx[score[1]]] = "Silver Medal"
        if len(score) > 2: ans[score_to_idx[score[2]]] = "Bronze Medal"

        for i in range(3, len(score)):
            ans[score_to_idx[score[i]]] = str(i+1)

        return ans
```

# Optimal Solution 
```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        # Pair each score with its original index
        indexed_scores = list(enumerate(score))
        # Sort descending by score
        indexed_scores.sort(key=lambda x: x[1], reverse=True)

        # Prepare the result array
        ans = [''] * n
        
        # Assign medals/ranks in one pass
        for rank, (idx, _) in enumerate(indexed_scores, start=1):
            if rank == 1:
                ans[idx] = "Gold Medal"
            elif rank == 2:
                ans[idx] = "Silver Medal"
            elif rank == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank)
        
        return ans
```
