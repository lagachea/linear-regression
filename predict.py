#! /usr/bin/python3
import pandas  as pd
from tools import import_thetas, estimate_price

mileage = input("Enter your mileage: ")
try:
    km = float(mileage)
except ValueError:
    km = 1234
    print(f"Your value: '{mileage}' could not be parsed as a float, default value {km} has been used")

theta_0, theta_1 = import_thetas()

price = estimate_price(km, theta_0, theta_1)

print(f"estimated price is: {price}")
