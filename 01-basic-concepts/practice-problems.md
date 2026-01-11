# Practice Problems: Basic Concepts

## Problem 1: Time Complexity Analysis
Analyze the time complexity of the following code snippets:

### 1.1
```python
def func1(n):
    for i in range(n):
        print(i)
```
**Answer:** O(n)

### 1.2
```python
def func2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```
**Answer:** O(n²)

### 1.3
```python
def func3(n):
    i = 1
    while i < n:
        i *= 2
        print(i)
```
**Answer:** O(log n)

### 1.4
```python
def func4(n):
    if n <= 1:
        return 1
    return func4(n-1) + func4(n-2)
```
**Answer:** O(2^n)

## Problem 2: Space Complexity Analysis
Analyze the space complexity of the following functions:

### 2.1
```python
def func1(n):
    total = 0
    for i in range(n):
        total += i
    return total
```
**Answer:** O(1)

### 2.2
```python
def func2(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr
```
**Answer:** O(n)

### 2.3
```python
def func3(n):
    if n <= 0:
        return 0
    return n + func3(n-1)
```
**Answer:** O(n) - due to recursion stack

## Problem 3: Algorithm Design
Design algorithms with the following requirements:

### 3.1 Find Maximum Element
- **Requirement:** Find the maximum element in an unsorted array
- **Target Complexity:** O(n) time, O(1) space
- **Solution:** Linear scan through the array

### 3.2 Check for Duplicates
- **Requirement:** Check if an array contains any duplicate elements
- **Target Complexity:** O(n) time, O(n) space
- **Solution:** Use a hash set to track seen elements

### 3.3 Count Occurrences
- **Requirement:** Count how many times each element appears in an array
- **Target Complexity:** O(n) time, O(n) space
- **Solution:** Use a dictionary/hash map

## Problem 4: Comparing Algorithms
Compare the following pairs of algorithms:

### 4.1 Linear Search vs Binary Search
- **When to use each?**
- **What are the trade-offs?**

### 4.2 Iterative vs Recursive
- **When is iteration better?**
- **When is recursion better?**
- **What are the space complexity implications?**

## Problem 5: Real-World Applications
Think about real-world scenarios where algorithm analysis matters:

1. **Searching:** Finding a contact in your phone (sorted vs unsorted)
2. **Sorting:** Organizing files by date vs by name
3. **Filtering:** Finding all items matching a criteria
4. **Optimization:** Finding the shortest path, maximum profit, etc.

## Solutions
Try to implement solutions for these problems in separate Python files:
- `solution-01-time-complexity.py`
- `solution-02-space-complexity.py`
- `solution-03-algorithm-design.py`
- `solution-04-comparing-algorithms.py`
