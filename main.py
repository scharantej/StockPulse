
from flask import Flask, render_template, request, Response
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historical_performance')
def historical_performance():
    return render_template('historical_performance.html')

@app.route('/live_updates')
def live_updates():
    def generate_updates():
        while True:
            stock_data = yf.download('^GSPC', period='1d', interval='1m')
            yield f"data: {stock_data.to_json()}\n\n"

    return Response(generate_updates(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
