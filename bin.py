import os
import config_coin_mpv

from binance.client import Client

# init
api_key = config_coin_mpv.api_key
api_secret = config_coin_mpv.api_secret

client = Client(api_key, api_secret)

print('<b>CARTERA</b><br/>')
print('<br/>')
wallet_sand=client.get_asset_balance(asset='SAND')
wallet_avax=client.get_asset_balance(asset='AVAX')
wallet_luna=client.get_asset_balance(asset='LUNA')
print('SAND: '+str(wallet_sand['free'])+'<br/>')
print('AVAX: '+str(wallet_avax['free'])+'<br/>')
print('LUNA: '+str(wallet_luna['free'])+'<br/>')
print('<br/>')
print('<b>PREUS</b><br/>')
print('<br/>')
sand_price = client.get_symbol_ticker(symbol="SANDUSDT")
print('Sand: ' + str(sand_price['price']) + '<br/>')
avax_price = client.get_symbol_ticker(symbol="AVAXUSDT")
print('Avax: ' + str(avax_price['price']) + '<br/>')
luna_price = client.get_symbol_ticker(symbol="LUNAUSDT")
print('Luna: ' + str(luna_price['price']) + '<br/>')

eurusd = client.get_symbol_ticker(symbol="EURUSDT")
eurusd_price = eurusd['price']
print('EuroUsd: ' + str(eurusd_price) + '<br/>')
print('<br/>')
print('<b>Wallet USD</b><br/>')
print('<br/>')
total_sand=float(sand_price['price'])*float(wallet_sand['free'])
total_avax=float(avax_price['price'])*float(wallet_avax['free'])
total_luna=float(luna_price['price'])*float(wallet_luna['free'])
print('SAND: ' + str(total_sand) + '<br/>')
print('AVAX: ' + str(total_avax) + '<br/>')
print('LUNA: ' + str(total_luna) + '<br/>')

total=total_sand+total_avax+total_luna
print('')
print('')
total_eur=float(total)/float(eurusd_price)
print('<br/>')
print('<b>TOTAL: ' + str(round(total_eur,2)) + ' € | ' + str(round(total,2)) + ' $</b>')
