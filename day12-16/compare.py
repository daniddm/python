from game_data import data
import random


def fromat_data(account):    
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    print(f"{account_name}, a {account_descr}, from {account_country}")


account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)