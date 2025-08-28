<h2><a href="https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors">2085. Array With Elements Not Equal to Average of Neighbors</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array <code>nums</code> of <strong>distinct</strong> integers. You want to rearrange the elements in the array such that every element in the rearranged array is <strong>not</strong> equal to the <strong>average</strong> of its neighbors.</p>

<p>More formally, the rearranged array should have the property such that for every <code>i</code> in the range <code>1 &lt;= i &lt; nums.length - 1</code>, <code>(nums[i-1] + nums[i+1]) / 2</code> is <strong>not</strong> equal to <code>nums[i]</code>.</p>

<p>Return <em><strong>any</strong> rearrangement of </em><code>nums</code><em> that meets the requirements</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> [1,2,4,5,3]
<strong>Explanation:</strong>
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,2,0,9,7]
<strong>Output:</strong> [9,7,6,2,0]
<strong>Explanation:</strong>
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
Note that the original array [6,2,0,9,7] also satisfies the conditions.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# **Wiggle Sort / Rearrange Array - Problem Solving Notes**

## **🎯 Problem Understanding**

### **Goal:**
Rearrange array so that `nums[0] < nums[1] > nums[2] < nums[3] > nums[4]...`
- Create alternating pattern: small-large-small-large...
- No specific ordering required, just the wiggle pattern

### **Key Insight:**
You need alternating "peaks" and "valleys" - not a specific arrangement

---

## **🧠 Two Main Approaches**

### **Approach 1: Sort + Swap Pairs**
**Strategy:**
1. Sort the entire array first
2. Swap adjacent pairs starting from index 1
3. Creates guaranteed wiggle pattern

**Why it works:**
- Sorting gives you ordering relationships
- Swapping pairs maintains these while creating peaks/valleys
- Pattern: `[a,b,c,d,e,f]` → `[a,c,b,e,d,f]`

**Complexity:** O(n log n) time, O(1) space

---

### **Approach 2: Greedy Single Pass (Optimal)**
**Strategy:**
1. Process array left to right in one pass
2. At each position, determine if it should be peak or valley
3. If current arrangement violates wiggle property, fix locally
4. Use greedy swapping to maintain pattern

**Key Patterns:**
- **Even indices (0,2,4...)**: Should be valleys (smaller than neighbors)
- **Odd indices (1,3,5...)**: Should be peaks (larger than neighbors)

**Why it works:**
- Local fixes don't break previous relationships
- Greedy choice is always optimal for wiggle property
- Each position only needs to satisfy constraint with previous position

**Complexity:** O(n) time, O(1) space

---

## **🔍 Critical Problem-Solving Insights**

### **1. Position-Based Logic**
- **Odd positions**: Must be greater than previous (peak)
- **Even positions**: Must be smaller than previous (valley)
- Check: `should_be_peak = (i % 2 == 1)`

### **2. Violation Detection**
```
If position i should be peak: nums[i] must be > nums[i-1]
If position i should be valley: nums[i] must be < nums[i-1]
```

### **3. Greedy Fix Strategy**
When violation found: **swap current with previous**
- Simple and always works
- Doesn't affect future positions
- Maintains previously established relationships

### **4. Why Local Fixes Work**
- Each swap only affects relationship between two adjacent elements
- Previous relationships remain intact
- Future positions can be handled independently

---

## **💡 Key Insights for Optimization**

### **1. No Global Sorting Needed**
- You don't need specific values at specific positions
- Just need relative ordering between adjacent elements
- Local comparisons and swaps are sufficient

### **2. Single Pass Sufficiency**
- Process each position exactly once
- Make greedy decision at each step
- No need to revisit previous positions

### **3. Pattern Recognition**
- Problem has repeating structure (peak-valley-peak-valley...)
- Use position parity (even/odd) to determine required relationship
- Consistent rule application across entire array

---

## **🎲 Edge Cases to Consider**

### **1. Array Length**
- **Length 1**: Always valid (no neighbors to compare)
- **Length 2**: Any arrangement works (just ensure nums[0] ≠ nums[1] if needed)

### **2. Duplicate Elements**
- Wiggle pattern still possible with duplicates
- Focus on inequality relationships, not strict ordering

### **3. Already Sorted Arrays**
- **Ascending**: Need to create peaks by swapping
- **Descending**: Need to create valleys by swapping

---

## **🚀 Optimization Progression**

### **Level 1 Thinking:** Sort entire array first
- Time: O(n log n)
- Works but overkill

### **Level 2 Thinking:** Recognize local pattern
- Each position has specific role (peak/valley)
- Can determine violations locally

### **Level 3 Thinking:** Greedy single pass
- Fix violations as you encounter them
- No need for global rearrangement
- Time: O(n) - optimal

---

## **🎯 Algorithm Pattern Recognition**

### **Problem Type:** Array rearrangement with local constraints
### **Technique:** Greedy local optimization
### **Key Skill:** Recognizing when local fixes create global solution
### **Optimization:** Trading global sorting for local swapping

**This problem teaches:** Sometimes complex-seeming rearrangements can be solved with simple greedy approaches when you identify the
`As long as the array is alternating (meaning the numbers go up and then down continuously until the end) it will fit the criteria`
```ini
I have solved this question in the most easiest way possibe.
1.Just sort the array in non-decreasing order
2.Start a for loop from index 1 and swap the value i+1 value that greater than ith value
3.Increment the for loop by i+=2
```
```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1

        while i < len(nums)-1:
            x, y = nums[i], nums[i+1]
            nums[i] = y
            nums[i+1] = x
            i += 2
        
        return nums
```
---
# Optimal Solution 
```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            should_be_peak = False
            if i % 2: should_be_peak = True
            
            a, b = nums[i], nums[i-1]
            
            if should_be_peak and a > b:
                continue
            elif not should_be_peak and a < b:
                continue
            else:
                    nums[i] = b
                    nums[i-1] = a
        
        return nums
```
---
```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            should_be_peak = False
            if i % 2: should_be_peak = True
            
            if should_be_peak and nums[i] < nums[i-1] or not should_be_peak and nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        
        return nums
```
