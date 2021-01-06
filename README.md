# etherScraper
#### Author: Jeet Chugh

###### etherScraper is a CLI program that finds an ethereum wallet's transactions using the etherscan.io API.
**Features:**
  - display ethereum network transactions onto the command line
  - View: **blockHash, txnHash, time, sender, reciever, etherAmount**
  - Lightweight, only uses requests, bs4, and datetime
#### [Github Repository Link]( https://github.com/Jeet-Chugh/etherScanner.git)ry``
Dependencies: *bs4, requests*
#### Code License: MIT
# Documentation
---
#### 'etherScraper' Class:
etherScraper takes in WALLET_ADDRESS and API_KEY, and returns a list of Transaction objects.
**Import:**
in the same directory --> ``from etherScraper import etherScraper``
**Instantiation:**
``wallet1 = etherScraper(WALLET_ADDRESS, API_KEY)``
#### **'etherScraper' Method:**
---
---
``wallet1.getData()``
returns a list of Transaction objects pertaining to the originally inputted WALLET_ADDRESS. Make sure to run main.py to have a better understanding of how the etherScraper(WALLET_ADDRESS, API_KEY).getData() method  works.
---

---
#### 'Transaction' Class:
The Transaction keeps txData organized in one object.
**Import:**
``from etherScraper import Transaction``
let tx be an instantiation of Transaction, in this example.
#### **'Transaction' Attrbutes:**
---
``tx.blockHash``
stores the block hash of the transaction.
---
``tx.txnHash``
stores the transaction hash of the transaction.
---
``tx.time``
stores a datetime object of the timestamp of the transaction. Can be converted to string by the datetime.datetime.sfrtime() method.
---
`tx.sender`
stores the Wallet Address of the sender in the transaction.
---
---
`tx.receiver`
stores the Wallet Address of the receiver in the transaction.
---
---
`tx.etherAmount`
In the case that the transaction is in Ether, it stores the amount of Ether transferred.
---
Thank you for reading the documentation. Feel free to submit issues to the repository URL listed above.
