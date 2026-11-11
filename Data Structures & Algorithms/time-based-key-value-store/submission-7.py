class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        # binary search the maximum time val in the timeMap <= timestamp
        l, r = 0, len(self.TimeMap[key]) - 1
        val = self.TimeMap[key]
        ret = ""
        while l <= r:
            m = (l + r) // 2
            if val[m][1] <= timestamp:
                # search right, but save l
                ret = val[m][0]
                l = m+1
            else:
                r = m-1
        
        return ret
        

        
        
