#write python program for a movie theater that charges different ticket prices based on charge.
age = int(input("Enter age:"))
if(age<5):
    print("Ticket price is 0(Free)")
elif(age>=5 and age<=12):
    print("Ticket price: $10")
elif(age>=13 and age<=60):
    print("Ticket price: $15")
else:
    print("Ticket price: $12")