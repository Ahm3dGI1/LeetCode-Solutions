class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
                continue

            if i < len(flowerbed)-1 and flowerbed[i+1] == 1:
                i += 3
                continue

            if i > 0 and flowerbed[i-1] == 1:
                i += 1
                continue
            n -= 1
            i += 2

        return n <= 0
