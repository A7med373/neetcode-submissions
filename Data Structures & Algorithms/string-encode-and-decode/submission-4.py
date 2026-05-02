class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '#' + s for s in strs)
    #  4#neet4#co d  e  4  #  l   o v e3#you
    #  0123456789 10 11 12 13 14 15 16
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1 
            result.append(s[i:i+length])
            i += length
        return result