class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1:
        count = {}

        # Step 2:
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3:
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 4:
        for n, c in count.items():
            buckets[c].append(n)

        res = []
        # 1) n -1 is the last index
        # 2) go all the way down to index 0
        # 3) -1 is the decrementor
        for freq in range(len(buckets) - 1, 0, -1):  
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res