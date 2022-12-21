# crypto-exchange-connector
Прослойка между Trading View Alerts и практически любой крипто-биржей. 

Инструкция:
1. Добавить "index.py", "requirements.txt", "config.py" в Яндекс функции.
2. В файле "index.py" можно изменить биржу или же futures на spot.
3. В файле "config.py" укажите: api key, secret key, tg bot token, tg chat id.
4. Настройте свою стратегию на Trading View (начальный капитал, комиссия и тд).
5. Включите будильники (используйте в формате файла "trading_view_alert.txt" - пару нужно прописать руками из-за особенностей CCXT).
