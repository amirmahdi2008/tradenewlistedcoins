# tradenewlistedcoins
You can trade automaticaly new listed coins at Kucoin Exchange or Mexc Exchange and make profit

Using this robot, you can buy and sell the currencies that are added to the Kucoin and Mexc exchanges as quickly as possible.
It is completely simple and automatic.

Usually, when digital currencies are listed, they will be very profitable in the first minute, and then their prices will drop drastically within a few minutes.
If you buy the currency exactly when it is listed and sell it less than a minute later, it will be very profitable for you.

It is better to entrust this work to this robot so that it buys and sells at the appointed time.

> [Kucoin New Listing](https://www.kucoin.com/news/categories/listing)

> [Mexc New Listing](https://support.mexc.com/hc/en-001/sections/360000547811-New-Listings)

With the help of this robot, you can buy and sell newly listed currencies in Kucoin and Mexc exchanges.

Before listing, these exchanges publish a notice about it, the address of Kucoin and Mexc exchange notices is placed above, and you can be aware of the new currencies and set the robot for them.

Prerequisites :
* [Python Version 3.9<](https://www.python.org/)
* [Mexc Python API SDK](https://github.com/mxcdevelop/mexc-api-sdk)
* [Kucoin Python API SDK](https://github.com/Kucoin/kucoin-python-sdk)
* Fast Internet

Using :
* Install Python 3.9
* Get Mexc python API SDK and put files & folders at project
* Get Kucoin python API SDK and put files & folders at project
* Set config.ini of robot
* Start main.py file
* Enter exchange name (mexc or kucoin)
* Enter new kucoin name (sample : btc)
* Enter time to buy (format : Year,Month,Day,Hour,Minute,Second)
* Enter Funds ( Minimum funds to buy from mexc is 5USDT and Minimum funds to buy from kucoin is 0.1USDT)
* Enter Sell At (That is, when the purchase is made successfully, how many seconds later will it be sold?) 

> Be careful, make sure to use a high-speed internet and make the settings of the robot several minutes before the new currency is listed.

>If you changed config.ini, you need to close and re-run main.py for the robot to apply the changes.
