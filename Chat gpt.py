# Hard-coded values
price = 6700
paid = 10000
change = paid - price

# coins
coin1000 = change // 1000
coin500 = (change % 1000) // 500
coin200 = (change % 500) // 200
coin100 = (change % 200) // 100

print("The price of your item is", price, "shillings, and your change is", change, "shillings.")
print("Here's the change that uses the fewest coins:\n")

print("1000 shillings:", coin1000)
print("500 shillings:", coin500)
print("200 shillings:", coin200)
print("100 shillings:", coin100)