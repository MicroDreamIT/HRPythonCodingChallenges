'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''
from django.template.defaultfilters import length


#   a b c a b c b b
#   0 1 2 3 4 5 6 7
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        i=0
        target_value = s[0]
        remaining_value = s[1:]
        length_remaining_value = len(remaining_value)
        # print(s, target_value, s.index(target_value))
        while i<length_remaining_value:
            # break
            if target_value in s:
                # print(s, i, length, target_value, remaining_value)
                location = remaining_value.index(target_value)
                remaining_value = remaining_value[location+1:]
                i=0
                target_value = remaining_value[0]
                print(s, i, length_remaining_value, target_value, remaining_value)
                # break
                if location > count + 1:
                    count = location + 1

            else:
                i += 1
            length_remaining_value = len(remaining_value)





        # for i in range(len(str_value)):
        #     str_value = s[i:]
        #     print(str_value, s[i])
        #     if s[i] in str_value:
        #         duplicate_index = str_value.index(str_value)
        #     else:
        #         duplicate_index = 0
        #     #
        #     if duplicate_index + 1 > count:
        #         count = duplicate_index + 1
        #         i = duplicate_index
        #
        # return count







if __name__ == '__main__':
    solution = Solution()
    value = solution.lengthOfLongestSubstring("abcabcbb")