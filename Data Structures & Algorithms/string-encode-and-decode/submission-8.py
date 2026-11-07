class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoding method will be "length" + "#" + "string"
        # e.g. Hello, World becomes "5#Hello5#World"

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
            

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0
        while i < len(s):
            # increment j until # is hit. that's the length, array slicing.
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        
        return res

        


            

