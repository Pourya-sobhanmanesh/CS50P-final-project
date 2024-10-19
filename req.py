import requests
from pprint import pprint

url = 'https://api.coincap.io/v2/assets'
api_key = 'b62751b6-510e-4f6b-ae4e-82e5e7899fa7'
encoding_methods = "gzip, deflate"

headers = {
    "Accept-Encoding" : encoding_methods,
    "Authorization" : f"Bearer {api_key}"
}


owned_crypto = {
    "cardano": 112.09,
    "solana": 0.8618,
    "pancakeswap": 14.81,
    "ethereum": 0.0104,
    "chainlink": 2.2520,
    "polkadot": 2.9542,
    "the-sandbox": 15.9340,
    "decentraland": 13.0269,
}



ids = [id for id in owned_crypto]

def main():
    pprint(search_req("btc"))

def get_by_id(*ids, url = url):
    url += "?ids="
    for id in ids:
        url += id + ","

    response = requests.get(url , headers = headers)

    if response.status_code == 200:
        response = response.json()["data"]
    else:
        print("Error!")

    response_dict = [{"id":crypto["id"], "symbol":crypto["symbol"], "name":crypto["name"], "priceusd": crypto["priceUsd"], "change_percent":crypto["changePercent24Hr"]} for crypto in response if crypto["id"] != ""]
    
    return response_dict


def search_req(name, url = url):
    url += "?search="
    url += name

    r = requests.get(url, headers = headers)

    if r.status_code == 200:
        r = r.json()["data"]
    else:
        print("Error")

    r_dict = [{"id":crypto["id"], "symbol":crypto["symbol"], "name":crypto["name"], "priceusd": crypto["priceUsd"], "change_percent":crypto["changePercent24Hr"]} for crypto in r]


    for i, c in enumerate(r_dict):
        if c["id"] == name.lower():
            print("found by name")
            index = i
            break
        elif c["symbol"] == name.upper():
            print("found by symbol")
            index = i
            break
        elif c["name"] == name.capitalize():
            print("found by name")
            index = i
            break
    else:
        index = None

    if index != None:
        return r_dict[index]
    else:
        return False

def get_by_search(*ids):
    list_of_cryptoes = []
    for id in ids:
        if result := search_req(id):
            list_of_cryptoes.append(result)
        else:
            print(f"could not find {id}")
    return list_of_cryptoes


if __name__ == "__main__":
    main()


