<h2><a href="https://leetcode.com/problems/minimum-index-sum-of-two-lists">599. Minimum Index Sum of Two Lists</a></h2><h3>Easy</h3><hr><p>Given two arrays of strings <code>list1</code> and <code>list2</code>, find the <strong>common strings with the least index sum</strong>.</p>

<p>A <strong>common string</strong> is a string that appeared in both <code>list1</code> and <code>list2</code>.</p>

<p>A <strong>common string with the least index sum</strong> is a common string such that if it appeared at <code>list1[i]</code> and <code>list2[j]</code> then <code>i + j</code> should be the minimum value among all the other <strong>common strings</strong>.</p>

<p>Return <em>all the <strong>common strings with the least index sum</strong></em>. Return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;Piatti&quot;,&quot;The Grill at Torrey Pines&quot;,&quot;Hungry Hunter Steakhouse&quot;,&quot;Shogun&quot;]
<strong>Output:</strong> [&quot;Shogun&quot;]
<strong>Explanation:</strong> The only common string is &quot;Shogun&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;Shogun&quot;,&quot;Tapioca Express&quot;,&quot;Burger King&quot;,&quot;KFC&quot;], list2 = [&quot;KFC&quot;,&quot;Shogun&quot;,&quot;Burger King&quot;]
<strong>Output:</strong> [&quot;Shogun&quot;]
<strong>Explanation:</strong> The common string with the least index sum is &quot;Shogun&quot; with index sum = (0 + 1) = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> list1 = [&quot;happy&quot;,&quot;sad&quot;,&quot;good&quot;], list2 = [&quot;sad&quot;,&quot;happy&quot;,&quot;good&quot;]
<strong>Output:</strong> [&quot;sad&quot;,&quot;happy&quot;]
<strong>Explanation:</strong> There are three common strings:
&quot;happy&quot; with index sum = (0 + 1) = 1.
&quot;sad&quot; with index sum = (1 + 0) = 1.
&quot;good&quot; with index sum = (2 + 2) = 4.
The strings with the least index sum are &quot;sad&quot; and &quot;happy&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= list1.length, list2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= list1[i].length, list2[i].length &lt;= 30</code></li>
	<li><code>list1[i]</code> and <code>list2[i]</code> consist of spaces <code>&#39; &#39;</code> and English letters.</li>
	<li>All the strings of <code>list1</code> are <strong>unique</strong>.</li>
	<li>All the strings of <code>list2</code> are <strong>unique</strong>.</li>
	<li>There is at least a common string between <code>list1</code> and <code>list2</code>.</li>
</ul>

# Solution 
* Firstly, we traverse over the whole list1 and create an entry for each element of list1 in a HashMap map, of the form (list[i],i). Here, i refers to the index of the ith element, and list[i] is the ith element itself. Thus, we create a mapping from the elements of list1 to their indices.

* Now, we traverse over list2. For every element ,list2[j], of list2 encountered, we check if the same element already exists as a key in the map. If so, it means that the element exists in both list1 and list2. Thus, we find out the sum of indices corresponding to this element in the two lists, given by sum=map.get(list2[j])+j. If this sum is less than the minimum sum obtained till now, we update the resultant list to be returned, res, with the element list2[j] as the only entry in it.

* If the sum is equal to the minimum sum obtained till now, we put an extra entry corresponding to the element list2[j] in the res list.

```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map_lst1 = {}
        comm_str = []
        min_idxSum = float('inf')

        for i,s in enumerate(list1):
            map_lst1[s] = i
        
        for i,s in enumerate(list2):
            if s in map_lst1:
                tmp_sum = i + map_lst1[s]
                
                if tmp_sum < min_idxSum:
                    comm_str = [s]
                    min_idxSum = tmp_sum
                elif tmp_sum == min_idxSum:
                    comm_str.append(s)
        
        return comm_str
```
