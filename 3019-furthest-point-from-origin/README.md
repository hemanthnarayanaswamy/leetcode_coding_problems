<h2><a href="https://leetcode.com/problems/furthest-point-from-origin">3019. Furthest Point From Origin</a></h2><h3>Easy</h3><hr><p>You are given a string <code>moves</code> of length <code>n</code> consisting only of characters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;_&#39;</code>. The string represents your movement on a number line starting from the origin <code>0</code>.</p>

<p>In the <code>i<sup>th</sup></code> move, you can choose one of the following directions:</p>

<ul>
	<li>move to the left if <code>moves[i] = &#39;L&#39;</code> or <code>moves[i] = &#39;_&#39;</code></li>
	<li>move to the right if <code>moves[i] = &#39;R&#39;</code> or <code>moves[i] = &#39;_&#39;</code></li>
</ul>

<p>Return <em>the <strong>distance from the origin</strong> of the <strong>furthest</strong> point you can get to after </em><code>n</code><em> moves</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;L_RL__R&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves &quot;LLRLLLR&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;_R__LL_&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves &quot;LRLLLLL&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;_______&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves &quot;RRRRRRR&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= moves.length == n &lt;= 50</code></li>
	<li><code>moves</code> consists only of characters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code> and <code>&#39;_&#39;</code>.</li>
</ul>

# Approach 
* To get the maximum distance we need to move in the same direction as much as possible because moving 1L and 1R will cancel out the distance, so travel to one side. 
* Now to decide which side to move depends on the given input with directions, Example here `"_R__LL_"` here we have traveled left more adding more L will increase the distance. 
* When both are equal anything is fine. 

# Solution
* First determine which direction to travel by default with which count is greater 
```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        if moves.count('R') > moves.count('L'):
            travelDirection = 'R' 
        else:
            travelDirection = 'L'

        directionsVal = {'R': 1, 'L': -1}
        
        dist = 0

        for d in moves:
            if d == '_':
                dist += directionsVal[travelDirection]
            else:
                dist += directionsVal[d]
        
        return abs(dist)
```

# Optimal Solution 
* The distance will be the difference between the count of R and L to see which is greater and then the count of "_" which fill it

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
```
