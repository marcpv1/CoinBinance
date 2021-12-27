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
sand_price = client.get_symbol_ticker(symbol="SANDUSDT")
avax_price = client.get_symbol_ticker(symbol="AVAXUSDT")
luna_price = client.get_symbol_ticker(symbol="LUNAUSDT")

eurusd = client.get_symbol_ticker(symbol="EURUSDT")
eurusd_price = eurusd['price']

total_sand=float(sand_price['price'])*float(wallet_sand['free'])
total_avax=float(avax_price['price'])*float(wallet_avax['free'])
total_luna=float(luna_price['price'])*float(wallet_luna['free'])

print('<a href="https://coinmarketcap.com/es/currencies/the-sandbox/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/6210.png\" width=\"40\" height=\"40\"></a>')
print('<b>The Sandbox</b><br/>')
print('(' + str(sand_price['price']) + ')<br/>')
print('Quantitat: ' + str(wallet_sand['free']) + '<br/>')
print('Saldo: ' + str(total_sand) + '<br/>')
print('<br/>')


print('<a href="https://coinmarketcap.com/es/currencies/avalanche/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/5805.png\" width=\"40\" height=\"40\"></a>')
print('<b>Avalanche</b><br/>')
print('(' + str(avax_price['price']) + ')<br/>')
print('Quantitat: ' + str(wallet_avax['free']) + '<br/>')
print('Saldo: ' + str(total_avax) + '<br/>')
print('<br/>')

print('<a href="https://coinmarketcap.com/es/currencies/terra-luna/" target="_blank">')
print('<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/4172.png\" width=\"40\" height=\"40\"></a>')
print('<b>Terra</b><br/>')
print('(' + str(luna_price['price']) + ')<br/>')
print('Quantitat: ' + str(wallet_luna['free']) + '<br/>')
print('Saldo: ' + str(total_luna) + '<br/>')

total=total_sand+total_avax+total_luna
print('')
total_eur=float(total)/float(eurusd_price)
print('<br/>')
print('<b>TOTAL: ' + str(round(total_eur,2)) + ' € | ' + str(round(total,2)) + ' $</b>')
