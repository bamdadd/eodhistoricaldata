from py_vollib.black.implied_volatility import implied_volatility
from py_vollib.black_scholes import black_scholes


class ImpliedVolatility:
    def __init__(self, chain):
        self.chain = chain

    def calculate(self):
        # price(float) – the Black - Scholes option price
        # S(float) – underlying asset price
        # K(float) – strike price
        # t(float) – time to expiration in years
        # r(float) – risk - free interest rate
        # flag(str) – ‘c’ or ‘p’ for call or put.
        price = black_scholes(flag, S, K, t, r, sigma)
        iv = implied_volatility(price, S, K, t, r, flag)
        return iv