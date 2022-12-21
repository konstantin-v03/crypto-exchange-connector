import config
import os
import requests
import json
import base64
import ccxt
import ast

"""Telegram Bot:"""
def tg_send_mess(bm):
    btoken = config.BOT_TOKEN
    bchat = config.CHAT_ID
    send = 'https://api.telegram.org/bot'+btoken+'/sendMessage?chat_id='+bchat+'&text='+bm+''
    resp = requests.get(send)
    return resp.json()


"""Decoding Message:"""
def run(event, context):
    try:

        """Decoding from TreadingView Format:"""
        mess = base64.b64decode(event['body']).decode('utf-8')

        s = mess.replace("'", "\"")
        d = ast.literal_eval(s)

        pare = d['pare']
        direct = d['direction']
        pos = d['position']
        # pos = round(float(d['position']),0)

        """Sedning Order to Exhcange:"""
        exchange = ccxt.binance({"apiKey": config.apiKey, "secret": config.secret,'options': {'defaultType': 'future'}})

        if direct == 'buy':
            exchange.create_market_buy_order(symbol=pare, amount=pos)
        if direct == 'sell':
            exchange.create_market_sell_order(symbol=pare, amount=pos)
        
        """Telegram Message:"""
        tg_send_mess(mess)

        """Checking for Errors:"""
        r = {'statusCode': 200, 'body': 'Message sent!'}
    except Exception as e:
        r = {'statusCode': 404, 'body': 'Some error!'}

    return r