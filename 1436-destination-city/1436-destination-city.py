class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l1 = set()
        l2 = set()
        for i in paths:
            l1.add(i[0])
            l2.add(i[1])
        return list(l2-l1)[0]