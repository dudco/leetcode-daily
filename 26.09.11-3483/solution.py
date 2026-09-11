class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        ret = set()

        def find(selected, depth, number):
            if depth == 3:
                ret.add(number)
                return
            for i, d in enumerate(digits):
                if i in selected: continue
                if depth == 2 and d ==0 : continue
                find([*selected, i], depth+1, number + (d * (10 ** depth)))
            
        for idx, d in enumerate(digits):
            if d % 2 == 1: continue
            find([idx], 1, d)

        return len(ret) 
