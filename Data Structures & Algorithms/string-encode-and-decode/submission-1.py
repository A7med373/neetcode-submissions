class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = str(len(strs[0])) + '#'
        for i in range(1, len(strs)):
            result += strs[i - 1] + str(len(strs[i])) + '#'
            if i == len(strs) - 1:
                result += strs[i]
        return result

    #  4#neet4#co d  e  4  #  l   o v e3#you
    #  0123456789 10 11 12 13 14 15 16
    def decode(self, s: str) -> List[str]:
        result = []
        i = int(s[0]) #4
        index = 2    #   2 : 6
        result.append(s[index:index+i])

        while True:
                # 2 + 4 
            if index + i < len(s) - 1:
                        # 2 + 4
                index += i #6
                i = int(s[index])
                index += 2 # 8        6+4
                result.append(s[index:index+i])
            if index + i - 1 == len(s) - 1:
                return result