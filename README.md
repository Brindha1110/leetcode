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
--------------------------------------------------------------------------------------------
## DAY 3:
       PROBLEM TITLE:
       Median of Two Sorted Arrays
       PROBLEM EXPLANATION:
       -The problem asks you to find the median of two sorted arrays after combining them.  In this solution, both arrays are merged into a single array and sorted. If the  total number of elements is odd, the middle element is returned as the median. If the total number of elements is even, the median is the average of the two middle elements.
--------------------------------------------------------------------------------------------

## DAY 4:
      PROBLEM TITLE:
        Roman to Integer
      PROBLEM EXPLANATION:
      -Create a dictionary to store the integer value of each Roman numeral symbol.
      -Traverse the Roman numeral string from left to right.
      -Compare the current symbol with the next symbol.
      -If the current value is smaller than the next value, subtract it from the total.
      -Return the final total as the integer representation of the Roman numeral.

----------------------------------------------------------------------------------------
## DAY 5:
    PROBLEM TITLE:
      Longest Common Prefix
    PROBLEM EXPLANATION:
    -Initialize the first string in the array as the common prefix.
    -Compare the prefix with each remaining string in the array.
    -If a string does not start with the current prefix, remove the last character from the prefix until it matches.
    -Return the final common prefix, or an empty string if no common prefix exists.
-------------------------------------------------------------------------------------------
## DAY 6:
     PROBLEM TITLE:
       Remove Duplicates from Sorted Array
     PROBLEM EXPLANATION:
    -The array nums is sorted in non-decreasing order, so duplicate elements appear next to each other.
    -The goal is to remove duplicates in-place without using extra space and return the number of unique elements (k).
    -The first k positions of nums should contain all the unique elements in their original order.
    -The values beyond the first k positions do not matter, since only k is used to verify the result.
--------------------------------------------------------------------------------------------
## DAY 7:
PROBLEM TITLE:
     Length of Last Word
PROBLEM EXPLANATION:
    -The problem is to find the length of the last word in a given string s.
    -A word is defined as a sequence of non-space characters.
    -The input string may contain leading spaces, trailing spaces, or multiple spaces between words.
    -While finding the last word, all extra spaces should be ignored.
    -The program should return the number of characters in the last word as an integer.
--------------------------------------------------------------------------------------------


     


