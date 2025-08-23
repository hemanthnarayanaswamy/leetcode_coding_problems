<h2><a href="https://leetcode.com/problems/asteroid-collision">735. Asteroid Collision</a></h2><h3>Medium</h3><hr><p>We are given an array <code>asteroids</code> of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.</p>

<p>For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.</p>

<p>Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [5,10,-5]
<strong>Output:</strong> [5,10]
<strong>Explanation:</strong> The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [8,-8]
<strong>Output:</strong> []
<strong>Explanation:</strong> The 8 and -8 collide exploding each other.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> asteroids = [10,2,-5]
<strong>Output:</strong> [10]
<strong>Explanation:</strong> The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= asteroids.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= asteroids[i] &lt;= 1000</code></li>
	<li><code>asteroids[i] != 0</code></li>
</ul>

# Solution 
<p> The Asteroid Collision problem can be considered a variation of the classic Balancing Symbols problem, although it might not be immediately apparent.

The Balancing Symbols problem is a classic problem where you have a sequence of symbols, such as parentheses, and you want to determine if they are "balanced". That is, for every opening symbol, there should be a corresponding closing symbol. One common way to solve this problem is by using a stack data structure.

In the case of the Asteroid Collision problem, the "opening" and "closing" symbols are replaced by positive and negative integers respectively, with positive integers moving right and negative integers moving left. We can imagine the problem as trying to determine if the movements of the asteroids are "balanced", similar to the parentheses in the Balancing Symbols problem. That is, for every right-moving asteroid, is there a corresponding left-moving asteroid that would collide with it, and vice versa.

Therefore, the stack can be used in a similar way: When we encounter a right-moving asteroid (positive integer), we push it into the stack. When we encounter a left-moving asteroid (negative integer), we compare it with the top of the stack. If the left-moving asteroid is larger, we pop the right-moving asteroid from the stack (analogous to matching and removing a pair of opening and closing symbols), and continue the process until the stack is empty or the top of the stack is a left-moving asteroid.

Thus, while the problems are different in their specific details, they share a common structure that allows us to apply similar problem-solving strategies. It's this underlying structure that allows us to identify the Asteroid Collision problem as a variation of the Balancing Symbols problem.
	</p>
	
```ini
The negative and positive value asteroids are jusst moving away from each other instead of hitting each other.

if the index of a positive asteroid is to the right of the index of a negative asteroid then no collision will happen.
if the index of a positive asteroid is to the left of the index of a negative asteriod then a collision will happen.
```
	
```python
	class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0

        while i < len(asteroids):
            leftA = asteroids[i]
            if stack and (stack[-1] > 0 and leftA < 0):
                rightA = stack[-1]
                if rightA < -leftA:
                    stack.pop()
                elif rightA > -leftA:
                    i += 1
                else:
                    stack.pop()
                    i += 1
            else:
                stack.append(leftA)
                i += 1

        return stack
```

---
# Improved Solution 
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()  
                elif stack[-1] == abs(asteroid):
                    stack.pop()  
                    asteroid = 0  
                    break
                else:  
                    asteroid = 0  
                    break
            
            if asteroid != 0: 
                stack.append(asteroid)
        
        return stack
```
