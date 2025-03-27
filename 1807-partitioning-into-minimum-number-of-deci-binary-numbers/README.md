<h2><a href="https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers">1807. Partitioning Into Minimum Number Of Deci-Binary Numbers</a></h2><h3>Medium</h3><hr><p>A decimal number is called <strong>deci-binary</strong> if each of its digits is either <code>0</code> or <code>1</code> without any leading zeros. For example, <code>101</code> and <code>1100</code> are <strong>deci-binary</strong>, while <code>112</code> and <code>3001</code> are not.</p>

<p>Given a string <code>n</code> that represents a positive decimal integer, return <em>the <strong>minimum</strong> number of positive <strong>deci-binary</strong> numbers needed so that they sum up to </em><code>n</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;32&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10 + 11 + 11 = 32
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;82734&quot;
<strong>Output:</strong> 8
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;27346209830709182346&quot;
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> consists of only digits.</li>
	<li><code>n</code> does not contain any leading zeros and represents a positive integer.</li>
</ul>

# <center>Solution Approach</center>
* The problem needs to be solved first with logic then the actuall code itself.

```
So let's say number 3761

1. First  iteration is: 1111
Note that we already have 1 at the last position, so from now on we can add only 0 to it
2. Second iteration 1110 (1111+1110 = 2221)
3. Third iteration: 1110 (2221 + 1110 = 3331)
4. Fourth iteration 
* Note that the first position already contains 3, so from now on we can add only 0 to it
* 0110 (3331 + 0110 = 3441)
5. Fifth Iteration: 0110 (3441 + 0110 = 3551)
6. Sixth Iteration: 0110 (3551 + 0110 = 3661)
7. Seventh Iteration
* Note that the second to the end position already contains 6, so from now on we can add only 0 to it
* 0100 (3661 + 0100 =  3761)

We disassembled the number 3761 to the binary components and did it in a way it would take the least number of operations. If you add all these numbers from step 1 to step 7 you will get the initial 3761 and it only took 7 steps

How it works?
As you spotted once we had precise value at any of the positions we just adding 0 to it. And this is the main idea. We always can increase the number by adding 1 to get what we want and use 0 for positions with values that already satisfy us. And this is why the maximum digit in the value is a correct answer.
```
* Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
* If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.
* Thus the answer is equal to the max digit.

```python
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
```
