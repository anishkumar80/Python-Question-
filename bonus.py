#A company give bonuses based on an employees experiences and performances rating
salary = float(input("Enter your salary:"))
exp_year = int(input("Enter Experience years:"))
if exp_year > 5:
    rating = int(input("Enter your performance rating:"))
    if(rating>8):
        print("You get 20% bonus.")
        print("Bonus amount is:", (salary*20)/100)
    elif(rating>=5 and rating<=8):
        print("You get 10% bonus")
        print("Bonus amount is:", (salary*10)/100)
    else:
        print("You get 5% bonus.")
        print("Bonus amount is:", (salary*5)/100)
else:
    print("You get 5% bonus.")
    print("Bonus amount is:", (salary*5)/100)