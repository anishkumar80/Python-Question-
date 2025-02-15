#Write python program that determines shipping charges based on the order amount and customer location.

order_amount = float(input("(amount in $)Enter Order Amount:"))
if(order_amount>100):
    print("Shipping fee is free")
    loc = input("is the location is international (yes / no):")
    if (loc=="yes" or loc=="YES" or loc=="Yes"):
       print("Handling fee is $10")
       print("Total order amount is:", order_amount + 10)
    else:
       print("No Handling fee")
       print(f"Total order amount is:{order_amount}")
else:
    print("Shipping fee is $5")
    loc = input("is the location is international (yes / no):")
    if (loc=="yes" or loc=="YES" or loc=="Yes"):
        print("Handling fee is $15")
        print("Total order amount is:", order_amount + 15 + 5)
    else:
        print("Total order amount is:", order_amount + 5)