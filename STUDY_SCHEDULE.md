# 5-Day Intensive Study Schedule
## Data Processing Algorithms (MAT 333/E)

**Target Audience:** Fast learner  
**Total Estimated Time:** ~29 hours over 5 days (~5.8 hours/day)  
**Study Approach:** Theory + Hands-on coding practice

---

## Day 1: Foundations (6 hours)
**Focus:** Building core algorithmic thinking and analysis skills

### Morning Session (3 hours)
**09:00 - 12:00**

#### 1. Basic Concepts (1.5 hours)
- **Read:** `01-basic-concepts/README.md`
- **Practice:**
  - `exercise-01-time-complexity.py` (30 min)
  - `exercise-02-space-complexity.py` (30 min)
  - `exercise-03-algorithm-comparison.py` (20 min)
  - `exercise-04-big-o-analysis.py` (10 min)
- **Key Concepts:** Time/space complexity, Big-O notation, algorithm comparison
- **Break:** 10 minutes

#### 2. Stable Matching (1.5 hours)
- **Read:** `02-stable-matching/README.md` + Textbook Chapter 1 (30 min)
- **Practice:**
  - `exercise-01-gale-shapley.py` (40 min)
  - `exercise-02-stable-matching-properties.py` (15 min)
  - `exercise-03-matching-applications.py` (5 min)
- **Key Concepts:** Gale-Shapley algorithm, stable matching properties, applications

### Afternoon Session (3 hours)
**13:00 - 16:00**

#### 3. Complexity Analysis (3 hours)
- **Read:** `03-complexity-analysis/README.md` + Textbook Chapter 2 (45 min)
- **Practice:**
  - `exercise-01-asymptotic-notation.py` (45 min)
  - `exercise-02-common-running-times.py` (45 min)
  - `exercise-03-tractability.py` (45 min)
- **Key Concepts:** Asymptotic notation (O, Ω, Θ), common running times, tractability
- **Review:** Summarize Day 1 concepts (15 min)

**Day 1 Total: 6 hours**

---

## Day 2: Graph Algorithms (5 hours)
**Focus:** Graph traversal, connectivity, and ordering

### Morning Session (2.5 hours)
**09:00 - 11:30**

#### 1. Graph Traversal (1.5 hours)
- **Read:** `04-graphs/README.md` + Textbook Chapter 3 (30 min)
- **Practice:**
  - `exercise-01-graph-traversal.py` (60 min)
    - Understand BFS vs DFS
    - Implement path finding
    - Practice on different graph structures
- **Key Concepts:** BFS, DFS, shortest paths in unweighted graphs

#### 2. Bipartiteness (1 hour)
- **Practice:**
  - `exercise-02-bipartiteness.py` (60 min)
    - Understand 2-coloring
    - Detect odd cycles
    - Apply to different graph types

### Afternoon Session (2.5 hours)
**13:00 - 15:30**

#### 3. Topological Ordering (1.5 hours)
- **Practice:**
  - `exercise-03-topological-ordering.py` (90 min)
    - Kahn's algorithm
    - DFS-based approach
    - Applications (course prerequisites, task scheduling)
- **Key Concepts:** DAGs, topological sort, cycle detection

#### 4. Review & Practice (1 hour)
- **Review:** All graph concepts
- **Challenge:** Solve graph problems from practice-problems.md (if available)
- **Self-test:** Implement BFS/DFS from scratch without looking

**Day 2 Total: 5 hours**

---

## Day 3: Greedy Algorithms (6 hours)
**Focus:** Greedy problem-solving strategies

### Morning Session (3 hours)
**09:00 - 12:00**

#### 1. Basic Greedy Problems (3 hours)
- **Read:** `05-greedy-algorithms/README.md` + Textbook Chapter 4 (30 min)
- **Practice:**
  - `exercise-01-coin-changing.py` (45 min)
    - Greedy vs DP comparison
    - When greedy works vs doesn't work
  - `exercise-02-interval-scheduling.py` (1.5 hours)
    - Interval scheduling
    - Interval partitioning
    - Minimize lateness
- **Key Concepts:** Greedy choice property, optimal substructure

### Afternoon Session (3 hours)
**13:00 - 16:00**

#### 2. Graph Greedy Algorithms (3 hours)
- **Practice:**
  - `exercise-03-dijkstra.py` (1.5 hours)
    - Shortest path algorithm
    - Path reconstruction
    - Applications (routing, navigation)
  - `exercise-04-mst.py` (1.5 hours)
    - Prim's algorithm
    - Kruskal's algorithm
    - Union-Find data structure
- **Key Concepts:** Shortest paths, minimum spanning trees, greedy graph algorithms

**Day 3 Total: 6 hours**

---

## Day 4: Divide & Conquer + Dynamic Programming I (6 hours)
**Focus:** Problem decomposition and optimization

### Morning Session (3 hours)
**09:00 - 12:00**

#### 1. Divide and Conquer (3 hours)
- **Read:** `06-divide-and-conquer/README.md` + Textbook Chapter 5 (30 min)
- **Practice:**
  - `exercise-01-mergesort-inversions.py` (1 hour)
    - Mergesort implementation
    - Counting inversions
  - `exercise-02-closest-pair.py` (1 hour)
    - Closest pair algorithm
    - Divide and conquer geometry
  - `exercise-03-master-theorem.py` (30 min)
    - Master theorem applications
    - Analyzing recurrences
- **Key Concepts:** Divide, conquer, combine; Master theorem

### Afternoon Session (3 hours)
**13:00 - 16:00**

#### 2. Dynamic Programming Introduction (3 hours)
- **Read:** `07-dynamic-programming/README.md` + Textbook Chapter 6 (30 min)
- **Practice:**
  - `exercise-01-fibonacci-paths.py` (1.5 hours)
    - Naive vs memoized vs bottom-up
    - Counting paths in grid
    - Understanding DP concepts
- **Key Concepts:** Overlapping subproblems, optimal substructure, memoization vs tabulation

**Day 4 Total: 6 hours**

---

## Day 5: Dynamic Programming II + Network Flow + Complexity Theory (6 hours)
**Focus:** Advanced DP, flow algorithms, and complexity classes

### Morning Session (3 hours)
**09:00 - 12:00**

#### 1. Advanced Dynamic Programming (2 hours)
- **Practice:**
  - `exercise-02-weighted-intervals.py` (1 hour)
    - Weighted interval scheduling
    - DP with intervals
  - `exercise-03-knapsack.py` (1 hour)
    - 0/1 Knapsack
    - Fractional knapsack (greedy)
    - Space optimization

#### 2. Network Flow (1 hour)
- **Read:** `08-network-flow/README.md` + Textbook Chapter 7 (20 min)
- **Practice:**
  - `exercise-01-ford-fulkerson.py` (40 min)
    - Ford-Fulkerson algorithm
    - Max-flow min-cut theorem
    - Bipartite matching via flow

### Afternoon Session (3 hours)
**13:00 - 16:00**

#### 3. Complexity Theory (2.5 hours)
- **Read:** `09-complexity-theory/README.md` + Textbook Chapter 8 (30 min)
- **Practice:**
  - `exercise-01-reductions.py` (1 hour)
    - Polynomial time reductions
    - Independent Set, Vertex Cover, Set Cover
  - `exercise-02-p-vs-np.py` (1 hour)
    - P vs NP problem
    - Complexity classes
    - Practical implications

#### 4. Final Review (30 min)
- **Review:** All major topics
- **Self-assessment:** Can you explain each algorithm?
- **Practice:** Quick implementation challenges

**Day 5 Total: 6 hours**

---

## Study Tips for Fast Learners

### 1. Active Learning Strategy
- **Code along:** Don't just read, implement each algorithm
- **Modify examples:** Change parameters, test edge cases
- **Explain out loud:** Teach concepts to yourself or others

### 2. Time Management
- **Pomodoro Technique:** 25 min focused study + 5 min break
- **Deep work blocks:** 2-3 hour sessions with minimal distractions
- **Review breaks:** 10-15 min breaks between major topics

### 3. Practice Approach
- **Run all exercises:** Execute code, understand output
- **Trace algorithms:** Step through with small examples
- **Compare approaches:** Understand when to use which algorithm

### 4. Retention Techniques
- **End-of-day summary:** Write 1-page summary of key concepts
- **Visual notes:** Create diagrams for complex algorithms
- **Flashcards:** Key algorithm complexities and properties

### 5. Assessment
- **Daily quiz:** Test yourself on previous day's material
- **Implementation challenge:** Re-implement algorithms from scratch
- **Problem solving:** Apply algorithms to new problems

---

## Quick Reference: Algorithm Complexities

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Gale-Shapley | O(n²) | O(n²) |
| BFS/DFS | O(V + E) | O(V) |
| Dijkstra | O((V+E)log V) | O(V) |
| Prim's MST | O((V+E)log V) | O(V) |
| Kruskal's MST | O(E log E) | O(V) |
| Mergesort | O(n log n) | O(n) |
| Closest Pair | O(n log² n) | O(n) |
| 0/1 Knapsack | O(n × W) | O(W) |
| Ford-Fulkerson | O(E × max_flow) | O(V + E) |

---

## Resources

### Primary
- **Textbook:** Algorithm Design by Kleinberg & Tardos
- **Exercises:** All exercise files in this repository
- **Syllabus:** `syllabus.md`

### Additional Practice
- LeetCode (greedy, DP, graph problems)
- HackerRank (algorithm challenges)
- Practice problems in `01-basic-concepts/practice-problems.md`

---

## Success Metrics

By the end of 5 days, you should be able to:
- ✅ Analyze time/space complexity of algorithms
- ✅ Implement BFS, DFS, Dijkstra, MST algorithms
- ✅ Apply greedy strategies to optimization problems
- ✅ Solve problems using divide and conquer
- ✅ Design dynamic programming solutions
- ✅ Understand network flow algorithms
- ✅ Explain P vs NP and complexity classes

---

## Adjustments for Your Pace

**If ahead of schedule:**
- Add more practice problems
- Implement additional algorithms from textbook
- Solve competitive programming problems

**If behind schedule:**
- Focus on core algorithms (skip some applications)
- Prioritize understanding over implementation
- Extend study time by 1-2 hours/day

**Good luck with your studies! 🚀**
