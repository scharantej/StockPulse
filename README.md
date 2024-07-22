## I want to build a web application that gives realtime updates about the S&P 500 stocks and then it will also give us it's historical perfomance.

### Flask Application Design

#### HTML Files

- **index.html**:
  - This file will serve as the application's home page.
  - It will contain a title and a brief introduction to the application.
  - It will also include a button that will allow the user to navigate to the historical performance page.

- **historical_performance.html**:
  - This file will display the historical performance of the S&P 500 stocks.
  - It will include a graph that shows the stock prices over time.
  - It will also include a table that shows the stock prices for each day.

#### Routes

- **@app.route('/')**:
  - This route will be mapped to the index.html file.
  - It will handle the request for the home page.

- **@app.route('/historical_performance')**:
  - This route will be mapped to the historical_performance.html file.
  - It will handle the request for the historical performance page.

- **@app.route('/live_updates')**:
  - This route will handle the request for live updates about the S&P 500 stocks.
  - It will use a streaming function to send real-time updates to the client.