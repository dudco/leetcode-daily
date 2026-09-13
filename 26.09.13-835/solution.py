class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        def make_bit(image: list[list[int]]):
            b = [0] * n
            
            for idx in range(n):
                for ei in range(n):
                    b[idx] += image[idx][n-ei-1] * (2 ** ei)

            return b

        def check(image1: list[int], image2: list[int]):
            cnt = 0
            for idx in range(n):
                cnt += (image1[idx] & image2[idx]).bit_count()

            return cnt

        def move_right(image: list[int]):
            r = image.copy()
            for idx in range(n):
                r[idx] = r[idx] >> 1

            return r

        def move_down(image: list[int]):
            d = image.copy()
            d = [0] + d[:n-1]
            return d

        def move_left(image: list[int]):
            l = image.copy()
            for idx in range(n):
                l[idx] = (l[idx] << 1) & ((2 ** n) - 1)

            return l

        def move_up(image: list[int]):
            u = image.copy()
            u = u[1:] + [0]
            return u
                        

        b_img1 = make_bit(img1)
        b_img2 = make_bit(img2)
        ret = check(b_img1, b_img2)

        b_img = b_img1.copy()
        for _ in range(n+1): # 30
            img = b_img.copy()
            c = check(img, b_img2) # 30
            ret = max(ret, c)
            
            for _ in range(n+1): # 30
                img = move_right(img) # 30
                c = check(img, b_img2) # 30
                ret = max(ret, c)
            b_img = move_down(b_img) 

        b_img = b_img1.copy()
        for _ in range(n+1): # 30
            img = b_img.copy()
            c = check(img, b_img2) # 30
            ret = max(ret, c)
            
            for _ in range(n+1): # 30
                img = move_right(img) # 30
                c = check(img, b_img2) # 30
                ret = max(ret, c)
            b_img = move_up(b_img) 

        b_img = b_img1.copy()
        for _ in range(n+1): # 30
            img = b_img.copy()
            c = check(img, b_img2) # 30
            ret = max(ret, c)
            
            for _ in range(n+1): # 30
                img = move_left(img) # 30
                c = check(img, b_img2) # 30
                ret = max(ret, c)
            b_img = move_down(b_img) 

        b_img = b_img1.copy()
        for _ in range(n+1): # 30
            img = b_img.copy()
            c = check(img, b_img2) # 30
            ret = max(ret, c)
            
            for _ in range(n+1): # 30
                img = move_left(img) # 30
                c = check(img, b_img2) # 30
                ret = max(ret, c)
            b_img = move_up(b_img) 

        return ret