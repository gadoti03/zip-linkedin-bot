class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        # per arrivare a n posso:
        # 1) togliere 1 a n
        # 2) togliere 2 a n
        # f restituisce un itero: numero di volte

        def f(n, d = {}) -> int:
            if n == -1:
                return 0 # case 1-2=-1
            if n == 0:
                return 1
            # if the result is in the dictonary
            if n in d:
                return d[n]
            # register the values in the dictonary
            d[n-1] = f(n-1, d)
            d[n-2] = f(n-2, d)
            # give the result
            return f(n-1, d) + f(n-2, d)
        return f(n)