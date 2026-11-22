"""438. 找到字符串中所有字母异位词
https://leetcode.cn/problems/find-all-anagrams-in-a-string/
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        raise NotImplementedError


if __name__ == "__main__":
    solution = Solution()
    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solution.findAnagrams("a", "ab") == []
    assert solution.findAnagrams("baa", "aa") == [1]
    print("ok")
