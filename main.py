from binance.client import Client
from binance.enums import *
from decimal import *
import time

#settings
BTC_amount = 0.05
api_key='xxx'
api_secret='xxx'

client = Client(api_key,api_secret)

def buy_all(currency):
    symbol=currency+'BTC'
    info=client.get_symbol_info(currency+'BTC')
    minimum=float(info['filters'][1]['minQty'])
    price_jump=float(info['filters'][0]['tickSize'])
    symbol=currency + 'BTC'
    buy_price=float(client.get_orderbook_ticker(symbol=symbol)['askPrice'])
    if minimum<1 : quantity = Decimal(BTC_amount/buy_price).quantize(Decimal(str(minimum)), rounding=ROUND_DOWN)
    else :         quantity = Decimal(BTC_amount/buy_price).quantize(Decimal('1.'), rounding=ROUND_DOWN)
    order = client.create_test_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
        )
    print('BUY order of ' + str(quantity) +' '+ str(symbol) +  ' set @ ' + str(buy_price) + ' BTC ' + ' totalling ' + str(buy_price*float(quantity))+ ' BTC ')
    time.sleep(1)
    sell_price=Decimal(1.2*buy_price).quantize(Decimal(str(price_jump)), rounding=ROUND_DOWN)
    order = client.create_test_order(
        symbol=currency + 'BTC',
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=quantity,
        price=sell_price
        )
    print('SELL order of ' + str(quantity) +' '+ str(symbol) +  ' set @ ' + str(sell_price) + ' BTC ' + ' totalling ' + str(sell_price*quantity)+ ' BTC ')

buy_all(input().upper())