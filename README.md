# Salomon Financial - FinTech App

## Project Proposal

**Salomon Financial** is a web application that serves as stock market simulator that allows users to get quotes, buy and sell stock. Created using the Flask web framework for Python as the web server and PSQL as the backend database. Front end design done with HTML and CSS (mostly Bootstrap). 
This web application targets newbie traders. They can use this app to simulate their trading strategy before investing real money on other apps like Robinhood, Sofi, etc...
The data that **Salomon Financial** will use a data-driven API to collect stock symbol, market price and volume. The API chosen for the project is **IEX Cloud** https://iexcloud.io/. 
My approach to creating this project is creating a database that will contain a table (users) with users and passwords, a table (stocks) with all stocks information, a table (transactions) that will serve as a log of all the transactions that will happen on this app, and a table (holding) with user ID and the stocks they hold.
The issue that we may experience with our chosen API is the fact that the users should always refresh the app to get the current market price. We are not sure that the market price would change instantly.
The functionalities of our app will include having an initial cash for $500,000.00 to invest, value of the portfolio( cash + investments). 
The user flow will be signing up, signing in, search for the stock the user is interested in, check the stock info(market price and volume) and buying stock or not. When an user signs in, she/he can access her/his portfolio and sell stocks and receive cash.
Our app is more that a CRUD because our app will have a good UI/UX and will help our users become financial independant.
The app has been deployed on Heroku and you can start paying right now by clicking on this link: https://salomon-financial.herokuapp.com/
We are open to feedbacks so we can continuously improve our app.
