# Data Structures and Algorithms Assignment 4: Graph Theory and Problem Solving

This repository contains my solutions for **Data Structures and Algorithms Assignment 4**, which focuses on solving graph theory problems and other algorithmic challenges. The assignment includes problems such as **Team Division in a Classroom**, **Dictionary Reordering**, **Travel Planning**, and **Museum Night Security**. Below is a detailed explanation of each problem and the corresponding solutions.

## 1. Team Division in a Classroom

The goal of this problem is to divide a classroom into two teams such that no two enemies are in the same team. This problem is modeled as a graph where each student is a node, and edges represent enmity between students. The solution involves checking if the graph is bipartite and then dividing the students into two teams accordingly.

### Approach:
- **Graph Representation**: The problem is represented as an undirected graph where edges denote enmity.
- **Bipartition Check**: Using a BFS-based approach, I checked if the graph is bipartite. If it is, the students can be divided into two teams without conflicts.
- **Output**: If bipartition is possible, the solution outputs the teams; otherwise, it returns `-1`.

## 2. Dictionary Reordering

This problem involves reordering a dictionary to match a desired sequence with the minimum number of operations. Each operation allows reversing a consecutive subsequence of the dictionary.

### Approach:
- **Problem Modeling**: The problem is modeled as finding the minimum number of reversals to transform one permutation into another.
- **Algorithm**: I used a BFS-based approach to explore the minimum number of operations required to reach the target permutation from the initial one.
- **Output**: For each test case, the solution outputs the minimum number of operations needed.

## 3. Travel Planning

The problem involves planning a trip through a tree-structured country, visiting all coastal cities and returning to the starting point. The goal is to determine if such a trip is possible and to output the sequence of cities visited.

### Approach:
- **Tree Traversal**: The problem is modeled as a tree traversal where the goal is to visit all leaf nodes and return to the root.
- **DFS Traversal**: I used a DFS-based approach to traverse the tree and generate the sequence of cities visited.
- **Output**: If a valid sequence exists, it is output; otherwise, `-1` is returned.

## 4. Museum Night Security

This problem involves navigating through a grid representing a museum, where some cells are dark and need to be illuminated. The goal is to find the minimum number of batteries required to light up the necessary rows or columns to reach the exit.

### Approach:
- **Grid Representation**: The museum is represented as a grid where some cells are initially lit, and others are dark.
- **BFS for Shortest Path**: I used a BFS-based approach to find the minimum number of row or column switches required to illuminate the path to the exit.
- **Output**: The solution outputs the minimum number of batteries needed or `-1` if it's impossible to reach the exit.

## Code Structure
The repository contains separate Python scripts for each problem:
- **Team Division**: Implementation of the bipartition check for the classroom problem.
- **Dictionary Reordering**: Algorithm for finding the minimum number of reversals.
- **Travel Planning**: Tree traversal to plan the trip through coastal cities.
- **Museum Night Security**: BFS-based solution for navigating the museum grid.
