class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        #as all the chars are small digit characters we can use a 26 0 wala hash map
        en=[0]*26
        for i in strs:
            en=[0]*26
            for c in i:
                en[ord(c)-ord('a')]+=1
            if tuple(en) in d:
                d[tuple(en)].append(i)
            else:
                d[tuple(en)]=[i]
        return list(d.values())