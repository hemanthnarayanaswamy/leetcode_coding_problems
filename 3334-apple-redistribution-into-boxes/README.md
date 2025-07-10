<h2><a href="https://leetcode.com/problems/apple-redistribution-into-boxes">3334. Apple Redistribution into Boxes</a></h2><h3>Easy</h3><hr><p>You are given an array <code>apple</code> of size <code>n</code> and an array <code>capacity</code> of size <code>m</code>.</p>

<p>There are <code>n</code> packs where the <code>i<sup>th</sup></code> pack contains <code>apple[i]</code> apples. There are <code>m</code> boxes as well, and the <code>i<sup>th</sup></code> box has a capacity of <code>capacity[i]</code> apples.</p>

<p>Return <em>the <strong>minimum</strong> number of boxes you need to select to redistribute these </em><code>n</code><em> packs of apples into boxes</em>.</p>

<p><strong>Note</strong> that, apples from the same pack can be distributed into different boxes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> apple = [1,3,2], capacity = [4,3,1,5,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> apple = [5,5,5], capacity = [2,4,2,7]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We will need to use all the boxes.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == apple.length &lt;= 50</code></li>
	<li><code>1 &lt;= m == capacity.length &lt;= 50</code></li>
	<li><code>1 &lt;= apple[i], capacity[i] &lt;= 50</code></li>
	<li>The input is generated such that it&#39;s possible to redistribute packs of apples into boxes.</li>
</ul>

# Solution 
* We need to store the apples in the boxes with different capacity and return the minimum number of total boxes required to store all the apples. 
* Note that, apples from the same pack can be distributed into different boxes. Based on this statement no matter the apple lot it can go to any box then Indeat of iteration we can get the total apples and then use that number to track the apples. 

1. While the total apples are greater then 0, totalApples is minus the highest of sorted Capacity and increment the box.
2. return the box 

```python
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacitySorted = sorted(capacity, reverse = True)

        totalApples = sum(apple)

        box = 0

        while totalApples > 0:
            totalApples -= capacitySorted[box]
            box += 1
        
        return box
```

```python
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        cnt_apple=sum(apple)
        capacity.sort(reverse=True)
        cnt=0

        for c in capacity:
            if cnt_apple <=0:
                break        
            cnt_apple-=c
            cnt+=1

        return cnt
```
