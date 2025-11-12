class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        # per arrivare a n posso:
        # 1) togliere 1 a n
        # 2) togliere 2 a n
        # f restituisce un intero: numero di modi

        def f(n, d = {}) -> int:
            if n == -1:
                return 0 # case 1-2=-1
            if n == 0:
                return 1
            # if the result is already in the dictionary
            if n in d:
                return d[n]
            # compute and register the value
            d[n] = f(n-1, d) + f(n-2, d)
            # give the result
            return d[n]

        return f(n)
