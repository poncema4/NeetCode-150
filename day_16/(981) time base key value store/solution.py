class TimeMap(object):

    def __init__(self):
        self.store = {} # key = list of [val, timestamp]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        values = self.store.get(key, [])

        # binary search for latest valid value
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            # [0] would be the value, [1] would be the timestamp
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)