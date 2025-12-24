class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse = True)

        cnt = 0
        for i in capacity:
            apples -= i
            cnt += 1
            if apples <= 0:
                return cnt
        
        return cnt