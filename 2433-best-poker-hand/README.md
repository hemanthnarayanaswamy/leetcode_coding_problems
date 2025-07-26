<h2><a href="https://leetcode.com/problems/best-poker-hand">2433. Best Poker Hand</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>ranks</code> and a character array <code>suits</code>. You have <code>5</code> cards where the <code>i<sup>th</sup></code> card has a rank of <code>ranks[i]</code> and a suit of <code>suits[i]</code>.</p>

<p>The following are the types of <strong>poker hands</strong> you can make from best to worst:</p>

<ol>
	<li><code>&quot;Flush&quot;</code>: Five cards of the same suit.</li>
	<li><code>&quot;Three of a Kind&quot;</code>: Three cards of the same rank.</li>
	<li><code>&quot;Pair&quot;</code>: Two cards of the same rank.</li>
	<li><code>&quot;High Card&quot;</code>: Any single card.</li>
</ol>

<p>Return <em>a string representing the <strong>best</strong> type of <strong>poker hand</strong> you can make with the given cards.</em></p>

<p><strong>Note</strong> that the return values are <strong>case-sensitive</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ranks = [13,2,3,1,9], suits = [&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;]
<strong>Output:</strong> &quot;Flush&quot;
<strong>Explanation:</strong> The hand with all the cards consists of 5 cards with the same suit, so we have a &quot;Flush&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ranks = [4,4,2,4,4], suits = [&quot;d&quot;,&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
<strong>Output:</strong> &quot;Three of a Kind&quot;
<strong>Explanation:</strong> The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a &quot;Three of a Kind&quot;.
Note that we could also make a &quot;Pair&quot; hand but &quot;Three of a Kind&quot; is a better hand.
Also note that other cards could be used to make the &quot;Three of a Kind&quot; hand.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> ranks = [10,10,2,12,9], suits = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;a&quot;,&quot;d&quot;]
<strong>Output:</strong> &quot;Pair&quot;
<strong>Explanation:</strong> The hand with the first and second card consists of 2 cards with the same rank, so we have a &quot;Pair&quot;.
Note that we cannot make a &quot;Flush&quot; or a &quot;Three of a Kind&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>ranks.length == suits.length == 5</code></li>
	<li><code>1 &lt;= ranks[i] &lt;= 13</code></li>
	<li><code>&#39;a&#39; &lt;= suits[i] &lt;= &#39;d&#39;</code></li>
	<li>No two cards have the same rank and suit.</li>
</ul>

# Solution 
### Step 1
If Five elements in suits are same return Flush so i used set for that with len()

### Step 2
I used `Counter()` for get the max value in ranks with it's frequency in dictionary

### Step 3
If value greater than 2 then i will return "Three of a Kind"
if value greater than 1 then i will return "Pair"
if value equals to 1 then i will return "High Card

```python
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        maxKind = max(Counter(ranks).values())

        if maxKind > 2:
            return "Three of a Kind"
        elif maxKind > 1:
            return "Pair"
        else:
            return "High Card"
```

# Creative Solution
```python
def bestHand(self, ranks: List[int], suits: List[str]) -> str:
	max_rank_cnt = max(Counter(ranks).values())
	max_suit_cnt = max(Counter(suits).values())

	return {
		max_rank_cnt == 2: 'Pair',
		max_rank_cnt >= 3: 'Three of a Kind',
		max_suit_cnt == 5: 'Flush',
	}.get(True, 'High Card')
```
* The above logic works in such a way, that the conditions inside the hashMap will be resolved to 

```ini
{True: 'Pair', False: 'Three of a Kind', False: 'Flush'}
now from the above dict it try to get which values is True 
that value will be returned 'Pair'

If not values is True then the "High Card" will be returned
```
