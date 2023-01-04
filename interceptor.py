#In The Creator Of Money | به نام آن که پول را آفرید

class interceptor:
    @staticmethod
    def exchange_coin_name(coin_name, base, exchange_name):
        if exchange_name == "kucoin":
            return coin_name + "-" + base
        elif exchange_name == "mexc":
            return coin_name + base

    @staticmethod
    def buy_time(timetext):
        return timetext.split(",")
