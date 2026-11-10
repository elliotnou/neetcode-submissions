class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # basically gets the string at the maximum timestamp in timemapp <= timestamp
        # use binary search, keep track of string at max
        ret = ""
        l, r = 0, len(self.timemap[key])-1
    
        while l <= r:
            val = self.timemap[key]
            m = (l+r)//2

            
            if val[m][1] <= timestamp:
                ret = val[m][0]
                l = m+1
            else:
                r = m-1
        return ret
            



