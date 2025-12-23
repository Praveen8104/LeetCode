class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        endtime = sorted(events, key = lambda x : x[1])
        n = len(events)
        max1 = [0] * n
        max1[0] = endtime[0][2]
        for i in range(1, n):
            max1[i] = max(max1[i - 1], endtime[i][2])

        ans = 0
        ind = 0
        for start, end, value in events:
            while ind < n and endtime[ind][1] < start:
                ind += 1
            ans = max(ans, value)
            if ind > 0:
                ans = max(ans, value + max1[ind - 1])
        return ans