class Solution:

    def encode(self, strs: List[str]) -> str:
        # to encode a list of strings, it must include information about the LENGTH of the string directly next to it ( a num) but since the string itself can contain number characters, the length and actual string should be separated with a special char, i.e. "#"
        # this way, decoding should be trivial(?) as you store the int strings until you hit this "#", then extract that length from the string
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        
        return ret

# 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            lenstr = ""
            while s[i] != "#":
                lenstr += s[i]
                i += 1
            i += 1
            j = i + int(lenstr)
            ret.append(s[i:j])
            i = j
        return ret
            
            

