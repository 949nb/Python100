
#Data Types

#String "Hello"[0]
#Integer 123
#Float 3.1415926
#Boolean True False

print("Welcome to the tip calculator.\n")
totalBill = input("What was the total bill?")
splitBillNum = input("How many people to split the bill?")
tipPercentage = input("What percentage tip would you like to give? 10, 12, or 15?")

payNum = (float(totalBill) + (float(totalBill) * float("0." + tipPercentage))) / int(splitBillNum)
print(f"Each person should pay: ${'{:.2f}'.format(round(payNum, 2))}")

