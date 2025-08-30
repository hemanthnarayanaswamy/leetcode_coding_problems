<h2><a href="https://leetcode.com/problems/pass-the-pillow">2645. Pass the Pillow</a></h2><h3>Easy</h3><hr><p>There are <code>n</code> people standing in a line labeled from <code>1</code> to <code>n</code>. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.</p>

<ul>
	<li>For example, once the pillow reaches the <code>n<sup>th</sup></code> person they pass it to the <code>n - 1<sup>th</sup></code> person, then to the <code>n - 2<sup>th</sup></code> person and so on.</li>
</ul>

<p>Given the two positive integers <code>n</code> and <code>time</code>, return <em>the index of the person holding the pillow after </em><code>time</code><em> seconds</em>.</p>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, time = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> People pass the pillow in the following way: 1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 3 -&gt; 2.
After five seconds, the 2<sup>nd</sup> person is holding the pillow.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, time = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> People pass the pillow in the following way: 1 -&gt; 2 -&gt; 3.
After two seconds, the 3<sup>r</sup><sup>d</sup> person is holding the pillow.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= time &lt;= 1000</code></li>
</ul>

# Solution
```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n -= 1
        m = time % n
        q = time // n

        if q % 2:
            return n - m + 1
        return m + 1
```

```ini
fullRounds = time / (n - 1) calculates how many complete rounds of passing occur.
extraTime = time % (n - 1) calculates the remaining time after complete rounds.
Check if fullRounds % 2 == 0:
If true, calculate the position as extraTime + 1.
If false, calculate the position as n - extraTime.
Return the position determined in the above step, which indicates the person holding the pillow after time seconds.
```

```python
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:                      # if there is only one person
            return 1                    # that person always holds the pillow

        # ------------------------------------------------------------------
        # What's next: Compute the cycle length of the back-and-forth walk.
        # The sequence goes 1..n and back to 1, which covers 2*(n-1) steps.
        # We'll reduce time modulo this cycle length to find the equivalent
        # position within a single cycle.
        # ------------------------------------------------------------------
        cycle = 2 * (n - 1)             # total steps in a full "bounce" cycle
        offset = time % cycle            # position within the repeating cycle

        # ------------------------------------------------------------------
        # What's next: If the offset is on the "forward" leg (from 1 up to
        # n), the holder is 1 + offset. Otherwise, we are on the "backward"
        # leg (from n down to 1), so compute the mirrored index as
        # 2*n - 1 - offset.
        # ------------------------------------------------------------------
        if offset <= n - 1:              # still moving forward from 1 to n
            return 1 + offset            # straightforward forward position
        else:                            # moving backward from n down to 1
            return 2 * n - 1 - offset
```

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/" target="_blank"> 3178: Find the Child Who Has the Ball After K Seconds.</a></p>
