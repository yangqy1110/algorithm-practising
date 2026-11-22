"""438. 找到字符串中所有字母异位词
https://leetcode.cn/problems/find-all-anagrams-in-a-string/
"""


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        size = len(p)
        if len(s) < size:
            return []
        target = Counter(p)
        window = Counter(s[:size])
        ans = []
        if window == target:
            ans.append(0)
        for i in range(size, len(s)):
            left = s[i - size]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            window[s[i]] += 1
            if window == target:
                ans.append(i - size + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solution.findAnagrams("a", "ab") == []
    assert solution.findAnagrams("baa", "aa") == [1]
    print("ok")
