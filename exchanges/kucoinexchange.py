#In The Creator Of Money | به نام آن که پول را آفرید

import time
from threading import Timer
from ini import ini

import kucoin.trade.trade as trade
import datetime

class kucoin_exchange:
    def __init__(self, time_to_buy, coin_name, funds, sell_at):

        self.time_to_buy = time_to_buy
        self.coin_name = coin_name
        self.funds = funds
        self.options = ini.configs()

        self.account = trade.TradeData(self.options['KUCOIN_KEY'], self.options['KUCOIN_SECRET'], self.options['KUCOIN_PASSWORD'])
        self.sell_at = sell_at

        now_date = datetime.datetime.now()
        now = datetime.datetime(now_date.year, now_date.month, now_date.day, now_date.hour, now_date.minute,now_date.second)

        target = datetime.datetime(int(time_to_buy[0]), int(time_to_buy[1]), int(time_to_buy[2]), int(time_to_buy[3]),
                                   int(time_to_buy[4]), int(time_to_buy[5]))

        remaning_time = (target - now).total_seconds()
        print("Waiting For Time " + str(remaning_time))

        self.start(remaning_time)

    def buy(self):

        print("ready for buy. in the creator of money")

        result = self.account.create_market_order(self.coin_name, 'buy', funds=self.funds)
        order = self.account.get_order_details(result['orderId'])

        print(f"Order Created , Symbol : {order['symbol']} ,  Funds : {order['funds']} , Price : {order['price']} , Size : {order['dealSize']} , Order_id : {order['id']}")

        order_complate = False

        while order_complate == False:

            details = self.account.get_order_details(result['orderId'])

            if details['isActive'] == False:
                order_complate = True

                print(f"Order Complate at {time.time()} , Wating and Set Sell Order {self.sell_at} Seconds")

                time.sleep(self.sell_at)

                self.sell(details['dealSize'])

    def sell(self, size):

        print("ready for sell. in the creator of money")

        result = self.account.create_market_order(self.coin_name, 'sell', size=size)
        order = self.account.get_order_details(result['orderId'])

        print(f"Order Created at {time.time()} , Symbol : {order['symbol']} , Funds : {order['funds']} , Price : {order['price']} ,  Size : {order['size']} , Order_id : {order['id']}")

        order_complate = False
        while order_complate == False:
            details = self.account.get_order_details(result['orderId'])
            if details['isActive'] == False:
                order_complate = True

                print(f"Order Complate at {time.time()}")

    def start(self, remaning):
        print("Starting Application , In The Name Of Creator Of Money")

        timer = Timer(remaning, self.buy)
        timer.start()
