'''

Code
Testcase
Testcase
Test Result
8. String to Integer (atoi)
Medium
Topics
Companies
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the
string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], then round the integer to remain in
the range. Specifically, integers less than -231 should be rounded to -2**31, and integers greater than 231 - 1
should be rounded to 231 - 1.
Return the integer as the final result.



Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.



Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''
from hackerRank.rr_2_breaking_the_record import result


class Solution:
    def myAtoi(self, s: str) -> int:
        value = 0
        s=s.lstrip()
        index = 0
        sign_multiplier = 1
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign_multiplier = -1
            index = 1
        if s[0] == '+':
            sign_multiplier = 1
            index=1

        while index < len(s):
            if not ('0'<= s[index] <= '9'):
                return value * sign_multiplier

            value = value * 10 + ord(s[index]) - ord('0')

            min_int_32 = 2**31
            if value*sign_multiplier <= -min_int_32:
                return -min_int_32
            if value*sign_multiplier >= min_int_32-1:
                return min_int_32-1

            index += 1

        return value*sign_multiplier

    '''
    Whitespace: Ignore any leading whitespace (" ").
    
    Signedness: Determine the sign by checking if the next character is '-' or '+', 
    assuming positivity if neither present.
    
    Conversion: Read the integer by skipping leading zeros until a non-digit character 
    is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
    then round the integer to remain in the range. Specifically, integers less than -231 
    should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
    '''


if __name__ == '__main__':
    test_cases = [
        # ("42", 42),
        (" -042", -42),
        # (" -042c3", -42),
        # ("1337c0d3", 1337),
        # ("0-1", 0),
        # ("words and 987", 0),
        # ("", 0),
        # ("   +42", 42),
        # ("   -42", -42),
        # ("   00042", 42),
        # ("-2147483649", -2147483648),  # Below the minimum 32-bit integer range
        # ("2147483648", 2147483647),  # Above the maximum 32-bit integer range
        # ("0000000000012345678", 12345678),
        # ("3.14", 3),
        # ("-3.14", -3),
        # ("+3.14", 3),
    ]
    solution = Solution()
    for case in test_cases:
        value = solution.myAtoi(case[0])
        print(value, value == case[1])
        # assert value == case[1]
