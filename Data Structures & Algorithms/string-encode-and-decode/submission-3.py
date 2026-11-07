class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoding method will be "length" + "#" + "string"
        # e.g. Hello, World becomes "5#Hello5#World"

        retstr = ""
        for s in strs:
            retstr += str(len(s)) + "#" + s
        return retstr
            

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])


    

            ret.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ret



            

