# Cryptocurrency Portfolio Tracker

#### Video Demo:  <URL HERE>

#### Description:
This program is a **Cryptocurrency Portfolio Tracker** that allows users to track the value of various cryptocurrencies in their portfolio. It retrieves real-time data from the [CoinCap API](https://docs.coincap.io/) and displays detailed information such as the current price, 24-hour change, and the total value of the cryptocurrencies in the user's portfolio.

### Features:
- Real-time cryptocurrency prices and market data.
- Displays total portfolio value.
- Search functionality to find specific cryptocurrencies.
- User-friendly GUI using `ttkbootstrap` for a themed interface.

### How to Install:
1. Clone the repository:
   ```bash
   git clone https://github.com/Pourya-sobhanmanesh/CS50P-final-project.git
   cd CS50P-final-project
2. Install the required dependencies
- Using pip:
    ```bash
   pip install -r requirements.txt
3. On Linux, make sure to install tkinter if it's not already installed:
- Ubuntu/Debian:
    ```bash
    sudo apt install python3-tk
- Fedora:
    ```bash
    sudo dnf install python3-tkinter

### How to Run:
- Run the main Python script:
    ```bash
    python project.py

### API:
The program uses the CoinCap API to fetch real-time data on cryptocurrency prices and market performance. To access this API, an API key is required, which should be included in the headers section of the script:
```python
api_key = 'your_api_key_here'
headers = {
"Accept-Encoding" : "gzip, deflate",
"Authorization" : f"Bearer {api_key}"
}

### Portfolio CSV:
The program reads a portfolio.csv file to get the amount of each cryptocurrency you own. The file should have the following format:
```csv
name,amount
bitcoin,0.5
ethereum,2

You can update the portfolio by editing this CSV file to reflect your current holdings.

### Additional Notes:
- Ensure you have an active internet connection to retrieve cryptocurrency data.
- Modify the portfolio.csv file to keep your portfolio up to date.

   


