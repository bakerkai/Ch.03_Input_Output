# gas mielage program
miles_driven = int(input("How long was your trip?"))
gallons_used = int(input("How many gallons of gas did you use?"))
mpg = miles_driven / gallons_used
print("Input from user", "Miles Driven = " , miles_driven ,"Gallons Used on Trip = " , gallons_used)
if mpg  > 17:
    print("You got good gas mileage!")
else:
     print("You got horrible gas mileage! Get rid of the junkbox and buy a prius!")
print(mpg, "Miles Per Gallon")


