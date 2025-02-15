#2 Write a python program that controls an air conditioning system based on the room temperature.

temperature = int(input("Enter Room temperature:"))
if(temperature>30):
    print("Turn on the AC.")
    if(temperature>40):
        print("set the AC to high cooling")
    else:
        print("Set the AC to normal")
elif(temperature>20 and temperature<30):
    print("keep the AC off")
else:
    print("Turn on the heater")