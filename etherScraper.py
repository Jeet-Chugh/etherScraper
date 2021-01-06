from requests import get as getRequest
from bs4 import BeautifulSoup
from datetime import datetime

class Transaction():

    def __init__(self, blockHash, txnHash, time, sender, receiver, etherAmount):
        self.blockHash = blockHash
        self.txnHash = txnHash
        self.time = time
        self.sender = sender
        self.receiver = receiver
        self.etherAmount = etherAmount

    def display(self):
        return \
        f"""        .-----------------------------------------------------------------------------------
        .Block Hash: {self.blockHash}
        .Transaction Hash: {self.txnHash}
        .Time: {self.time}
        .Sender: {self.sender}
        .Reciever: {self.receiver}
        .Amount (in Ethereum): {self.etherAmount}
        .-----------------------------------------------------------------------------------\n""".replace("        .", "")

class etherScraper():

    def __init__(self, WALLET_ADDRESS, API_KEY):
        self.WALLET_ADDRESS = WALLET_ADDRESS
        self.API_KEY = API_KEY

    def __getAPI__(self):
        URL = f"https://api.etherscan.io/api?module=account&action=txlist&address={self.WALLET_ADDRESS}&sort=asc&apikey={self.API_KEY}"
        request = getRequest(URL)
        result = BeautifulSoup(request.content, 'lxml').find("p").get_text()
        data = eval(result)["result"]
        if data == []:
            raise ValueError("Invalid Wallet Address")
        elif data == "Invalid API Key":
            raise ValueError("Invalid API Key")
        return data

    def getData(self):
        data = self.__getAPI__()
        result = []
        for tx in data:
            try:
                if tx["isError"] == '1':
                    continue

                amount = round(float(tx["value"]) / 10e17, 6)
                time = datetime.fromtimestamp(int(tx["timeStamp"]))

                new_tx = Transaction(blockHash=tx["blockHash"],
                                     txnHash=tx["hash"],
                                     time=time,
                                     sender=tx["from"],
                                     receiver=tx["to"],
                                     etherAmount=amount)
                result.append(new_tx)
            except:  result.append("Error")
        return result
