class TimeMap:
    # let the timemap be {key : list of [value, timestamp]}

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # we want the value from the time LESS THAN OR EQUAL TO the timestamp
        # searching every entry in the key's list is O(n)
        # we know the timestamps are increasing, so its somewhere between. we binary search

        val = self.timemap[key]
        l, r = 0, len(val) - 1
        ret = ""
        while l <= r:
            m = (l+r) // 2
            if val[m][1] <= timestamp:
                ret = val[m][0]
                l = m+1
            else:
                r = m-1
        
        return ret
        
