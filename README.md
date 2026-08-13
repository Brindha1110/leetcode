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
## DAY 8:
   PROBLEM TITLE:
      Plus One
PROBLEM EXPLANATION:
     -A problem definition is a clear statement that describes the issue or challenge that needs to be solved.
    -It identifies the gap between the current situation and the desired outcome.
    -A good problem definition explains who is affected and why the problem is important.
    -It provides a clear focus for developing effective solutions.
------------------------------------------------------------------------------------------- 
## DAY 9:
PROBLEM TITLE:
    Add Binary
PROBLEM EXPLANATION:
   -The problem is to add two binary numbers given as strings.
   -The solution must return their sum as a binary string without converting them to decimal.
   -It should correctly handle binary addition, including carry values.
   -The algorithm should work efficiently for binary strings of different lengths.
--------------------------------------------------------------------------------------------   
## DAY 10:
PROBLEM TITLE:
    Sqrt(X)
PROBLEM EXPLANATION:
    -The problem is to find the integer square root of a non-negative integer x without using built-in square root functions.
    -This solution uses binary search to efficiently search for the correct square root.
     If mid × mid is less than or equal to x, it stores mid as the current answer and searches the right half.
    -Finally, it returns the largest integer whose square is less than or equal to x in O(log x) time and O(1) space.
-----------------------------------------------------------------------------------------------
## DAY 11:
PROBLEM TITLE:
    Zigzag Conversion
PROBLEM EXPLANATION:
    -If numRows is 1 or greater than the string length, return the original string.
    -Create a list rows to store characters for each row of the zigzag pattern.
    -Traverse each character, adding it to the current row.
    -Reverse the direction whenever the top or bottom row is reached, then move to the next row.
    -Concatenate all rows using ''.join(rows) and return the final zigzag-converted string.
-----------------------------------------------------------------------------------------------
## DAY 12:
PROBLEM TITLE:
    Container With Most Water
PROBLEM EXPLANATION:
    -Initialize two pointers: left at the beginning and right at the end of the array.
    -Calculate the water area using width × min(height[left], height[right]).
    -Update max_water if the current area is larger than the previous maximum.
    -Move the pointer with the shorter height inward, since only that can potentially increase the area.
    -Repeat until the pointers meet, then return max_water.
    Time Complexity: O(n)
    Space Complexity: O(1)
-----------------------------------------------------------------------------------------------
## DAY 13:
PROBLEM TITLE:
Remove Duplicates from Sorted List
PROBLEM EXPLANATION:
   -You are given the head of a sorted singly linked list, where the nodes are arranged in non-decreasing order.
   -Since the list is sorted, any duplicate values will always appear consecutively.
   Your task is to remove the duplicate nodes so that each distinct value appears only once in the list.
   -The relative order of the remaining nodes should not be changed, and only the extra duplicate nodes should be removed.
   -Return the head of the modified linked list containing only unique elements.
-------------------------------------------------------------------------------------------## DAY 14:
PROBLEM TITLE:
Reverse Integer
PROBLEM EXPLANATION:
   -The problem occurs because the current system or process does not meet the required needs.
   -This leads to delays, errors, or reduced efficiency in completing tasks.
   -Users face difficulties in achieving the desired outcome quickly and accurately.
   -Existing solutions may be costly, time-consuming, or lack important features.
    -Therefore, a better solution is needed to improve performance, reliability, and user experience
-------------------------------------------------------------------------------------------
## DAY 15:
PROBLEM TITLE:
String to Integer(atoi)
PROBLEM EXPLANATION:
  -Given a 32-bit signed integer x, reverse its digits and return the reversed integer.
   -If x is negative, the reversed number should also remain negative.
   -While reversing, ensure the result stays within the 32-bit signed integer range (-2³¹ to 2³¹ - 1).
   -If reversing the integer causes an overflow, return 0.
   -The solution should efficiently reverse the digits using arithmetic operations without converting the integer to a string
-------------------------------------------------------------------------------------------
## DAY 16:
PROBLEM TITLE:
Longest Palindromic Substring
PROBLEM EXPLANATION:
   -Given a string s, find the longest substring that is a palindrome.
    -A palindrome is a string that reads the same forward and backward (e.g., "aba", "bb").
   -The substring must be continuous within the original string.
   -If there are multiple longest palindromes, returning any one of them is acceptable.
   -The goal is to return the longest palindromic substring.
--------------------------------------------------------------------------------------------
## DAY 17:
PROBLEM TITLE:
Longest Substring Without Repeating Characters
PROBLEM EXPLANATION:
  -Given a string s, find the length of the longest substring without repeating characters.
   -A substring must be a continuous sequence of characters.
  -The substring should contain only unique characters, with no duplicates.
  -Return the maximum possible length of such a substring.
  -For example, if s = "abcabcbb", the answer is 3 because "abc" is the longest substring without repeating characters
--------------------------------------------------------------------------------------------
## DAY 18:
PROBLEM TITLE:
Palindrome Number
PROBLEM EXPLANATION:
   -Given an integer x, determine whether it reads the same forward and backward.
   -A palindrome number remains unchanged when its digits are reversed (e.g., 121, 1331).
   -Negative numbers are not palindromes because the minus sign appears only at the beginning.
   -Numbers ending with 0 (except 0 itself) also cannot be palindromes since they would start with 0 after reversing.
   -The goal is to return True if x is a palindrome; otherwise, return False
--------------------------------------------------------------------------------------------------
DAY 19:
PROBLEM TITLE:
Integer to Roman
PROBLEM EXPLANATION:
   -The problem is to convert a given integer num into its Roman numeral representation.
   -We store Roman values and symbols in roman_map from largest to smallest.
   -For each value, num // value finds how many times that Roman symbol can be used.
   -We add the symbol to result and update num using num %= value.
   -We repeat this process until num becomes 0, using a greedy approach.
   -Finally, we join all the symbols in result and return the Roman numeral
----------------------------------------------------------------------------------------------------
## DAY 20:
PROBLEM TITLE:
Find First and Last Position of Element in Sorted Array
PROBLEM EXPLANATION:
   -The problem is to find the *first and last position* of a target value in a sorted array.
   -We use *binary search* instead of scanning the entire array, making the solution efficient.
   -The findBound() function searches for either the first or last occurrence using the isFirst flag.
   -When the target is found, we store its index and continue searching left for the first occurrence or right for the last occurrence.
   -If the target does not exist, the function returns [-1, -1].
   -Since binary search is performed twice, the overall *time complexity is O(log n)* and space complexity is *O(1)*
---------------------------------------------------------------------------------------------------
 ## DAY 21:
PROBLEM TITLE:
Remove Element
PROBLEM EXPLANATION:
    -The problem asks us to remove all occurrences of val from the array
    -We use k to track the position where the next valid element should go
    -We loop through every element using i
    -If nums[i] is not equal to val, we copy it to nums[k]
    -Then, we increase k because we placed one valid element
    -Finally, k is returned as the number of elements remaining
----------------------------------------------------------------------------------------------------
## DAY 22:
PROBLEM TITLE:
Pascal's Triangle
PROBLEM EXPLANATION:









     


