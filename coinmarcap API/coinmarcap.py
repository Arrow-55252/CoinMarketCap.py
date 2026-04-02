
import requests
from dotenv import load_dotenv
import os

class CryptoAPI:



    def main_info(self):

        load_dotenv()


        limit_input = input("How many cryptos do you want to see?\nType none if you want to skip. ").strip().lower()

        #Error Handling for limit_input
        if limit_input == "none" or limit_input == "":
            limit_num = 1000
            show_list = False

        elif limit_input.isdigit():
            limit_num = int(limit_input)
            show_list = True

        else:
            print("Please Try again")
            return
        

        #API Call
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?limit={int(limit_num)}"
        headers = {
            'Accept': 'application/json',
            'X-CMC_PRO_API_KEY':os.getenv('X-CMC_PRO_API_KEY')
        }
 
        r = requests.get(url, headers=headers)

        data = r.json()["data"]
        

        if show_list:
            self.crypto_list(data)
        else:
            self.crypto_name(data)

        return data
    

    def crypto_list(self, data=None):

            for info in data:

                print(f"\nid: {info["id"]}\nname: {info["name"]}\nsymbol: {info["symbol"]}\nmarket_cap: {int(info["quote"]["USD"]["market_cap"]):,}")



    def crypto_name(self, data=None):

        crypto_input = input("Type in name of crypto or symbol? " ).strip().lower()
        #Checks if the user has entered into the input
        if crypto_input:
            found = False
            for info in data:
                #Checking if crypto input matches a crypto slug or symbol in the dataset
                if crypto_input in (info["name"]).lower() or crypto_input in (info["symbol"]).lower():

                    print(f"\nid: {info["id"]}\nname: {info["name"]}\nsymbol: {info["symbol"]}\nmarket cap: ${int(info["quote"]["USD"]["market_cap"]):,}")
                    found = True
                #Error handling if crypto input does not match any crypto slug or symbol               
            if not found:
                print("Sorry the cryptocurrency could not be found.")

        else:
            print("Sorry, please try again")




user = CryptoAPI()
user.main_info()

        



