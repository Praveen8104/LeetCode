class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print(d)
        l = []
        cnt = 0
        for i in d.keys():
            if cnt == k:
                break
            l.append(i)
            cnt += 1
        return l
