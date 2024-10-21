# Cryptocurrency Portfolio Tracker

### Video Demo:  <URL HERE>

### Description:
This Cryptocurrency Portfolio Tracker lets users track their crypto investments by getting real-time data from the CoinCap API. It shows the current price, 24-hour changes, and calculates the total value of your portfolio.

It also has a search feature to look up specific cryptocurrencies by name, symbol, or ID, and get information like price, rank, and 24-hour change.

### Features:
- Real-time cryptocurrency prices and market data.
- Displays total portfolio value.
- Search functionality to find specific cryptocurrencies.
- User-friendly GUI using `tkinter`
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
```
### Portfolio CSV:
The program reads a portfolio.csv file to get the amount of each cryptocurrency you own. The file should have the following format:
```csv
name,amount
bitcoin,0.5
ethereum,2
```
You can update the portfolio by editing this CSV file to reflect your current holdings.

### Project Files:
- **portfolio.csv:** This file contains your cryptocurrency holdings. It is a CSV file where each row represents a cryptocurrency (name) and the amount you own.

- **project.py:** This is the main Python script that runs the cryptocurrency tracker. It includes the logic for fetching cryptocurrency data, processing your portfolio, and displaying the information in a graphical user interface (GUI).

- **README.md:** The file you're reading right now. It provides an overview of the project, how to install dependencies, how to run the program, and explanations of the project's files.

- **req.py:** This file originally contained functions related to handling API requests, but the functions were later copied to `project.py` to comply with the format requirements of the final project. It is kept here as a backup or reference.

- **requirements.txt:** This file lists all the Python dependencies required to run the project. You can install them using:

    ```bash
    pip install -r requirements.txt
    ```
- **./test/:** This directory contains testing-related files and configurations for the project. Unit tests and other test scripts are likely stored here.

- **test_project.py:** This is a test script that contains unit tests for the main program (project.py). Running this script ensures that the main functions of the program work as expected.

### Additional Notes:
- Ensure you have an active internet connection to retrieve cryptocurrency data.
- Modify the portfolio.csv file to keep your portfolio up to date.

### additional functions:
- **get_by_id(*ids, url=url)**:
    - Fetches cryptocurrency data for the specified ids from the CoinCap API.

    - The function returns a dictionary containing the extracted information for each cryptocurrency.The function returns a dictionary containing the extracted information for each cryptocurrency.
- **search_req(name, url=url)**:
    - Searches for a specific cryptocurrency by its name, symbol, or ID

    - This function appends the search term to the CoinCap API URL and sends a GET request. It returns a dictionary with details about the cryptocurrency such as ID, symbol, name, price in USD, and 24-hour percentage change.
    
    - It also checks if the search term matches the cryptocurrency's name, symbol, or ID and returns the first match it finds.

- **get_by_search(*ids)**:
    - This function takes in a list of cryptocurrency names, symbols, or IDs and performs a search using search_req().

    - It returns a list of cryptocurrencies that match the search criteria.
