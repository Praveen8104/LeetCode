class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = int("".join(f"{ord(char) - ord('a') + 1}" for char in s))
        
        while k > 0:
            num = sum(int(digit) for digit in str(num))
            k -= 1
            
        return num
