"""3. 无重复字符的最长子串
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, ans, length = {}, 0, 0
        for i, char in enumerate(s):
            length = min(length + 1, i - last.get(char, -1))
            last[char] = i
            ans = max(ans, length)
        return ans


if __name__ == "__main__":
    solution = Solution()
    for text, expected in [
        ("", 0), ("abba", 2), ("abcabcbb", 3), ("bbbbb", 1),
        ("pwwkew", 3), (" ", 1), ("dvdf", 3), ("你好你", 2),
    ]:
        assert solution.lengthOfLongestSubstring(text) == expected
    print("ok")
