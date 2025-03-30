price_item_1=float(input("enter the 1st item's maximum retail price : "))
discount_1 = float(input("enter the disount -1 : "))

price_item_2=float(input("enter the 2nd item's maximum retail price : "))
discount_2 = float(input("enter the disount -2 : "))

price_item_3=float(input("enter the 3rd item's maximum retail price : "))
discount_3 = float(input("enter the disount -3 : "))

price_item_4=float(input("enter the 4th item's maximum retail price : "))
discount_4 = float(input("enter the disount -4 : "))

price_item_5=float(input("enter the 5th item's maximum retail price : "))
discount_5 = float(input("enter the disount -5 : "))

payable_1 =  price_item_1 - (price_item_1*discount_1)/100
payable_2 =  price_item_2 - (price_item_2*discount_2)/100
payable_3 =  price_item_3 - (price_item_3*discount_3)/100
payable_4 =  price_item_4 - (price_item_4*discount_4)/100
payable_5 =  price_item_5 - (price_item_5*discount_5)/100

total = payable_1 + payable_2 + payable_3 + payable_4 + payable_5

sgst = 5 
cgst = 8

total = total + (sgst*total/100)+ (cgst*total/100)

total = round(total)

print("total payable amount ",total)

