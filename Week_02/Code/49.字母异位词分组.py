# 1. 当且仅当它们的排序字符串相等时，两个字符串是字母异位词。
class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for item in strs:
            key = tuple(sorted(item))
            dic[key] = dic.get(key, []) + [item]
        return list(dic.values())

# 2. 当且仅当它们的字符计数（每个字符的出现次数）相同时，两个字符串是字母异位词。
class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)] = dic.get(tuple(count), []) + [s]
        return list(dic.values())