import random
import time 
from datetime import datetime

users = [
    "U1001",
    "U1002",
    "U1003",
    "U1004",
    "U1005",
    "U1006",
    "U1007",
    "U1008",
    "U1009",
    "U1010"
]

merchants = [
    "Keells",
    "Cargills",
    "Dialog",
    "Uber",
    "PickMe",
    "Amazon",
    "Daraz",
    "Apple",
    "Netflix",
    "Spotify"
]

currencies = [
    "LKR",
    "USD",
    "EUR"
]

transaction_types = [
    "PURCHASE",
    "TRANSFER",
    "WITHDRAWAL",
    "PAYMENT"
]

statuses = [
    "SUCCESS",
    "FAILED",
    "PENDING"
]

print(random.choice(users))
print(random.choice(merchants))
print(random.choice(currencies))
print(random.choice(transaction_types))
print(random.choice(statuses))