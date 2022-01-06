"""
Problem Statement: Write a program that takes an array $A$ and an index $i$ into $A$, 
and rearranges the elements such that all elements less than $A[i]$ appears first, 
followed by elements equal to $A[i]$, followed by elements greater than $A[i]$.
"""

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified: A[equal:larger]
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
             A[smaller], A[equal] = A[equal], A[smaller]
             smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A

### Sample Inputs
print(dutch_flag_partition(1, [1,4,2,7,4,5,9,2,3,1]))

# (Potential) Output: [1, 2, 1, 3, 2, 4, 4, 9, 5, 7]
# A[1] = 4, bottom group = [1, 2, 1, 3, 2], middle group = [4,4]

"""
Each iteration decreases the size of unclassified by 1, and the time spent within each iteration is $O(1)$, implying:
- Time Complexity: $O(N)$
- Space Complexity: $O(1)$
"""