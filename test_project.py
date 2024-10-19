import pytest
from project import *
import csv
import os

def test_search_req():
    assert search_req("btc")["name"] == "Bitcoin" 
    assert search_req("bitcoiN")["name"] =="Bitcoin"
    assert search_req("Bitcoin")["name"] =="Bitcoin"

def test_search_req_not_found():
    assert search_req("hhhhhhhhhhhhhhh") == False 
    assert search_req("aaaaaaaaaaaaaaaa") == False

def test_read_csv():
    os.makedirs("./test", exist_ok=True)

    with open("./test/test_portfolio.csv", "w") as file:
        w = csv.DictWriter(file, fieldnames=["name", "amount"])
        w.writeheader()
        w.writerow({"name":"BTC", "amount": 1})
        w.writerow({"name":"sol", "amount": 2.5})
        w.writerow({"name":"cardano", "amount": 20.25})

    with open("./test/test_portfolio.csv", 'r') as file:
        r = read_csv("./test/test_portfolio.csv")
        for i, row in enumerate(r):
            if i == 0:
                assert row["name"] == "Bitcoin"
                assert row["amount"] == 1.0
                assert row["id"] == "bitcoin"
            if i == 1:
                assert row["name"] == "Solana"
                assert row["amount"] == 2.5
                assert row["id"] == "solana"

            if i == 2:
                assert row["name"] == "Cardano"
                assert row["amount"] == 20.25
                assert row["id"] == "cardano"

def test_read_csv_errors():
    os.makedirs("./test", exist_ok=True)
    path = "./test/test_portfolio.csv"

    with open(path, "w") as file:
        w = csv.DictWriter(file, fieldnames=["name", "amount"])
        w.writeheader()
        w.writerow({"name":"BTC", "amount": "ver much"})
        w.writerow({"name":"sol", "amount": 2.5})
        w.writerow({"name":"cardano", "amount": 20.25})

    with open(path, 'r') as file:
            with pytest.raises(ValueError):
                read_csv(path)
    
    with open(path, "w") as file:
        w = csv.DictWriter(file, fieldnames=["name", "amount"])
        w.writeheader()
        w.writerow({"name":"BTC", "amount": 1.254})
        w.writerow({"name":"sol", "amount": 2.5})
        w.writerow({"name":"cardanoooooooo", "amount": 20.25})

    with open(path, 'r') as file:
            with pytest.raises(CryptoNotFound):
                read_csv(path)
    
    with open(path, "w") as file:
        w = csv.DictWriter(file, fieldnames=["name", "amount"])
        w.writeheader()
        w.writerow({"name":"BTC", "amount": 0})
        w.writerow({"name":"sol", "amount": -2.5})
        w.writerow({"name":"cardano", "amount": 20.25})

    with open(path, 'r') as file:
            with pytest.raises(NotPositiveError):
                read_csv(path)

def test_return_final_dict():
    os.makedirs("./test", exist_ok=True)
    path = "./test/test_portfolio.csv"

    with open(path, "w") as file:
        w = csv.DictWriter(file, fieldnames=["name", "amount"])
        w.writeheader()
        w.writerow({"name":"BTC", "amount": 1})
        w.writerow({"name":"sol", "amount": 2.5})
        w.writerow({"name":"cardano", "amount": 20.25})
    
    row_1 = return_final_dict(read_csv(path))[0]
    row_2 = return_final_dict(read_csv(path))[1]
    row_3 = return_final_dict(read_csv(path))[2]

    assert round(float(row_1["total_val"]), 2) ==  round(float(row_1["amount"]) * float(row_1["priceusd"]), 2)
    assert round(float(row_2["total_val"]), 2) ==  round(float(row_2["amount"]) * float(row_2["priceusd"]), 2)
    assert round(float(row_3["total_val"]), 2) ==  round(float(row_3["amount"]) * float(row_3["priceusd"]), 2)


def test_calculate_total_value_all():
    os.makedirs("./test", exist_ok=True)
    path = "./test/test_portfolio.csv"

    with open(path, "w") as file:
        w = csv.DictWriter(file, fieldnames=["name", "amount"])
        w.writeheader()
        w.writerow({"name":"BTC", "amount": 1})
        w.writerow({"name":"sol", "amount": 2.5})
        w.writerow({"name":"cardano", "amount": 20.25})

    final_dict = return_final_dict(read_csv(path))
    final_val = 0
    for row in final_dict:
        final_val += float(row["total_val"])
    assert calculate_total_value_all(final_dict) == round(final_val, 2)




