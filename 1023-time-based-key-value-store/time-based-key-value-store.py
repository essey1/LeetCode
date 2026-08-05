class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = -1
        l, r = 0, len(self.time_map[key])-1
        while l<=r:
            mid = (l+r)//2
            if timestamp == self.time_map[key][mid][0]:
                return self.time_map[key][mid][1]
            elif timestamp < self.time_map[key][mid][0]:
                r = mid-1
            elif timestamp > self.time_map[key][mid][0]:
                idx = max(idx, mid)
                l = mid+1
        if idx == -1:
            return ""
        return self.time_map[key][idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)