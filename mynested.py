#If you are testing multiple conditions, an if/else statement will not 
# work. We use an if/elif.....else

#Take an input from a user.Test for high(>70), medium(>40<70) or low(<40)
#In addition to what you have above. Ensure the number entered 
# by user falls between 0 and 100
mynum = float(input("Enter number to test: "))
if (mynum>=0) and (mynum<=100):
    if mynum > 70:
        print("High")
    elif mynum < 70 and mynum > 40:
        print("Medium")
    else:
        print("Low")
else:
    print("number invalid")
#TASK
#CREATE A FILE CALLED mylargest.py TAKE INPUT FROM USER 3 NUMBERS 
# SEPARATELY. PRINTN THE LARGEST OF THE 3. IF ALL ARE EQUAL, PRINT EQUAL.




