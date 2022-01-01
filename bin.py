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
wallet_egld=client.get_asset_balance(asset='EGLD')
sand_price = client.get_symbol_ticker(symbol="SANDUSDT")
avax_price = client.get_symbol_ticker(symbol="AVAXUSDT")
luna_price = client.get_symbol_ticker(symbol="LUNAUSDT")
egld_price = client.get_symbol_ticker(symbol="EGLDUSDT")

eurusd = client.get_symbol_ticker(symbol="EURUSDT")
eurusd_price = eurusd['price']

total_sand=float(sand_price['price'])*float(wallet_sand['free'])
total_avax=float(avax_price['price'])*float(wallet_avax['free'])
total_luna=float(luna_price['price'])*float(wallet_luna['free'])
total_egld=float(egld_price['price'])*float(wallet_egld['free'])

print('<a href="https://coinmarketcap.com/es/currencies/elrond-egld/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/6892.png\" width=\"40\" height=\"40\"></a>')
print('<b>Elrond eGold</b><br/>')
print('(' + str(round(float(egld_price['price']),2)) + ' $)<br/>')
print('Quantitat: ' + str(wallet_egld['free']) + '<br/>')
print('Saldo: ' + str(round(total_egld,2)) + ' $<br/>')
print('<br/>')

print('<a href="https://coinmarketcap.com/es/currencies/the-sandbox/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/6210.png\" width=\"40\" height=\"40\"></a>')
print('<b>The Sandbox</b><br/>')
print('(' + str(round(float(sand_price['price']),2)) + ' $)<br/>')
print('Quantitat: ' + str(wallet_sand['free']) + '<br/>')
print('Saldo: ' + str(round(total_sand,2)) + ' $<br/>')
print('<br/>')


print('<a href="https://coinmarketcap.com/es/currencies/avalanche/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/5805.png\" width=\"40\" height=\"40\"></a>')
print('<b>Avalanche</b><br/>')
print('(' + str(round(float(avax_price['price']),2)) + ' $)<br/>')
print('Quantitat: ' + str(wallet_avax['free']) + '<br/>')
print('Saldo: ' + str(round(total_avax,2)) + ' $<br/>')
print('<br/>')

print('<a href="https://coinmarketcap.com/es/currencies/terra-luna/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/4172.png\" width=\"40\" height=\"40\"></a>')
print('<b>Terra</b><br/>')
print('(' + str(round(float(luna_price['price']),2)) + ' $)<br/>')
print('Quantitat: ' + str(wallet_luna['free']) + '<br/>')
print('Saldo: ' + str(round(total_luna,2)) + ' $<br/>')

total=total_sand+total_avax+total_luna+total_egld
print('')
total_eur=float(total)/float(eurusd_price)
print('<br/>')
print('<b>TOTAL: ' + str(round(total_eur,2)) + ' € | ' + str(round(total,2)) + ' $</b>')
