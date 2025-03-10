class Solution:
    def convertDateToBinary(self, date: str) -> str:
        sep = date.split('-')
        for i in range(len(sep)):
            if sep[i][0] == 0:
                del sep[i][0]
        lst = '-'.join([str(bin(int(el))).replace('0b','') for el in sep])
        return lst