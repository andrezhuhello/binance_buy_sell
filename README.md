# Binance quick buy/sell

## Prerequisities

```
python-binance
```

You can install it with pip
```
pip install python-binance
```
## What does it do ?
By default it will buy 0.05BTC worth of input currency at market rate and set a sell order with 20% profit. It should work with expensive and cheap currencies (ETH vs TRX - Jan 2018 ;) ) taking into account price and lot filters in Binance API.

## Running the script

Firstly change 'create_test_order' to 'create_order' if you want to do it "live" , current settings are for test orders.

Just run it in the terminal:

```
python3 main.py
```

and input the name of crypt you want to buy/sell

after it's finished you should get :

```
BUY order of 7002 TRXBTC set @ 7.14e-06 BTC 
SELL order of 7002 TRXBTC set @ 0.00000856 BTC 
```


BINANCE REFLINK : https://www.binance.com/?ref=11779127

ETH : 0x4Eb7F19D6eFcACE59EaED70220da5002709f9B71
