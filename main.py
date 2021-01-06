from etherScraper import etherScraper, Transaction

# Required Credentials
WALLET_ADDRESS = "" # WALLET THAT YOU WANT TO SEARCH THROUGH
API_KEY = ""        # ETHERSCAN API KEY

# Instantiate the Scraper, and fetch the Data
scraper = etherScraper(WALLET_ADDRESS, API_KEY)
transactions = scraper.getData()

# Display the Transactions in a CLI-Friendly manner
for tx in transactions:
    try:  print(tx.display())
    except:  print("\nerror\n")
