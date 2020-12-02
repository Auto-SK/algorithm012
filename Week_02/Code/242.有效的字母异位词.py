# 1. 判断 s 和 t 长度是否相等
# 2. 记录 s 中每个字母的个数，counter++
# 3. 记录 t 中每个字母的个数，counter--
# 4. 如果 counter < 0，说明 t 中某个字母个数比 s 多
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        counter = [0] * 26
        for i in s:
            counter[ord(i) - ord('a')] += 1
        for j in t:
            counter[ord(j) - ord('a')] -= 1
            if counter[ord(j) - ord('a')] < 0:
                return False
        return True