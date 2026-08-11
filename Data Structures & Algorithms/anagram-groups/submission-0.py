class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            if tuple(sorted(i)) in d:
                d[tuple(sorted(i))].append(i)
            else:
                d[tuple(sorted(i))]=[i]
        return list(d.values())