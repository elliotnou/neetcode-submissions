class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

            

    def decode(self, s: str) -> List[str]:
        5#hello5#world
        res = []
        i = 0
        while i < len(s)-1:
            j = i
            while s[j] != '#':
                j += 1
            
            print(s[i:j])
            lenstr = int(s[i:j])
            
            res.append(s[j+1:j+1+lenstr])
            i = j + 1 + lenstr
        
        return res
            


        


            

