# set needs to add the string to the key but also bind the string to a lookupable timestamp

# perhaps two a dictionaries, where {k1 : {k2 : v}}, k1 is name, k2 is timestamp, k3 is string

#
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        # binary search along timemap[key][m][1] -- the timestamps
        l, r = 0, len(self.timemap[key]) - 1
        
        maxtime = 0
        res = ""
        while l <= r:
            m = (l + r) // 2
            if timestamp >= self.timemap[key][m][1]:
                # acceptable, save
                res = self.timemap[key][m][0]
                l = m+1
            else:
                r = m-1
        
        return res


        
