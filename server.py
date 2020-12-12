import os
import json
from flask import Flask
from kucoin.client import Market

client = Market(url='https://api.kucoin.com')

app = Flask(__name__)

@app.route('/')
def hello_world():
	klines = client.get_kline('BTC-USDT','1min')
	return json.dumps(klines)

@app.route('/test')
def hello_world2():
	return "Bonjour Lucy"


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
