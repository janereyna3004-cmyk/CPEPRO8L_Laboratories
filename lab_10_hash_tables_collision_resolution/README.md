
# Laboratory Activity No. 10: Hash Tables and Collision Resolution

**Name:** Mary Jane Y. Reyna  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Date:** September 6, 2026

## Objectives

1. Implement a custom hash function.
2. Resolve collisions using linked-list chaining.
3. Understand how the load factor affects hash table performance.
4. Demonstrate insertion and searching operations.

## Program Description

This Python program implements a hash table using a custom hash function based on the sum of ASCII values of the characters in a key. It handles collisions through linked-list chaining and supports inserting, searching, displaying, and updating entries.

## How to Run
Run this command:

```bash
py lab10_hash_table.py
```

## Expected Output

```text
HASH TABLE: CHAINING
Bucket 0: [Bob: 30]
Bucket 1: [Charlie: 35]
Bucket 2:
Bucket 3: [Alice: 25] -> [Eve: 28]
Bucket 4:

SEARCH RESULTS
Alice: 25
Bob: 30
Charlie: 35
David: None

LOAD FACTOR
Entries: 4
Capacity: 5
Load factor: 0.80
```

## Collision Demonstration

Alice and Eve both produce bucket index 3.

- Alice: 478 % 5 = 3
- Eve: 288 % 5 = 3

The two entries are stored in the same bucket using a linked list. This prevents one entry from overwriting the other.

## Load Factor

The load factor is calculated by dividing the number of entries by the table capacity.

Load Factor = 4 / 5 = 0.80

This means that four entries are stored in a hash table with five buckets.

## Analysis Questions

### 1. Record hash table entries demonstrating a collision event.

Alice and Eve cause a collision because both keys map to bucket 3. Chaining stores both entries in the same bucket using linked-list nodes.

### 2. Compare the search efficiency of chaining versus linear probing.

Chaining stores colliding entries in a linked list, while linear probing searches for another available array position. Both methods can achieve average O(1) search time with a good hash function and a suitable load factor. In the worst case, search time can reach O(n). Linear probing can also suffer from clustering, while chaining requires additional memory for linked-list nodes.

## Conclusion

This activity demonstrated hash table insertion, searching, collision resolution, and load factor calculation. Chaining allows multiple keys to share a bucket without losing stored values. It also helped explain the differences between chaining and linear probing.
```

