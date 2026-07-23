## DAY 1:
    PROBLEM TITLE:
      Two sum
    PROBLEM EXPLANATION:
      -Loop through every pair of numbers in the array using two nested loops.
      -Check if the sum of the current pair equals the target value.
      -If it matches, return the indices of those two numbers; otherwise continue until a valid pair is found.
------------------------------------------------------------------------------------------- 

## DAY 2:
    PROBLEM TITLE:
       Add two number
    PROBLEM EXPLANATION:
       -Traverse both linked lists simultaneously, adding corresponding digits along with the carry from the previous addition.
       -Create a new node with total % 10, update the carry as total // 10, and attach the node to the result list.
       -Continue until both lists and the carry are exhausted, then return the result starting from dummy.next
----------------------------------------------------------------------------------------------------       