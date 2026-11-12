class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)   

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        # binary search, if it's bigger timestamp save in s
        val = self.TimeMap[key]
        l, r = 0, len(val)-1
        while l <= r:
            m = (l+r) // 2
            if val[m][1] <= timestamp:
                ret = val[m][0]
                l = m+1
            else:
                r = m-1
        
        return ret
            


        
