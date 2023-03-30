# imported forex python api
from forex_python.converter import CurrencyRates
import datetime


current_datetime = datetime.datetime.now()
cur_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')


# I want to convert aud to npr but in this api no npr
# so i coverted aud to inr and then inr to npr
# aud = australia
# npr = nepal
# inr = india

cr = CurrencyRates()

print(f"Conversion aud to npr as {cur_time}")
print("\n__________________________\n")
user = float(input("\taud: "))
inr = cr.convert('AUD','INR',user)
npr = round(inr * 1.60,2)
print("\tnpr:",npr)
print("\n__________________________")

