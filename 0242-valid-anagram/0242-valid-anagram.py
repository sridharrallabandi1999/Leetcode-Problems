class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        
        if len(s) != len(t): return False
        s_counter, t_counter = Counter(s), Counter(t)
        for c in s_counter:
            if s_counter[c] != t_counter[c]: return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        