#calculator to sum untill we enter quit

sum = 0
while(True):
    userInput = input("Enter the price or press q to exit: \n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
        
    else:
        print(f"Your Bill total is {sum}.Thanks for using our calculator. ")
        break