class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoding method will be "length" + "#" + "string"
        # e.g. Hello, World becomes "5#Hello5#World"

        retstr = ""
        for s in strs:
            retstr += str(len(s)) + "#" + s
        return retstr
            

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        
        while i < len(s):
            j = 0
            lenstr = ''
            while s[j+i] != '#':
                lenstr += s[i+j]
                j += 1
            
            i += j+1 # skip over the hashtag
            
            length = int(lenstr)
            word = ""
            while length > 0:
                word += s[i]
                i += 1
                length -= 1
            
            ret.append(word)
            
        return ret

            

