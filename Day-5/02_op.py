item_1 =  float(input("enter the mrp of item : "))
discount = float(input("enter discount in percentage : "))

payable_1 = item_1 - (item_1*discount)/100

print(round(payable_1))
