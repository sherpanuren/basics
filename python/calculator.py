#calculator to sum untill we enter quit
items = []
sum = 0

print("ABC Stores")

while(True):
    userInput = input("Enter the price or press q to exit: ")
    
    if (userInput != 'q'):
         price = int(userInput)
         items.append(price)     # adds price to the list
         sum = sum + price
         print(f"Order total so far: {sum}")
    else:
        print("\nReceipt:")
        print("ABC Store")
        
        for item in items:
            print(item)           #displays the individual items
        print(f"Your total is {sum}.")
        print(f"Thanks for using our calculator. ")
        break
