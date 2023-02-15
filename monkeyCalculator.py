def calculateTime():
    
    # This first line is provided for you
    
    monkey_one = input("Is the first monkey smiling?:  ").lower()
    monkey_two = input("Is the second monkey smiling?: ").lower()

    
    # end assignment
    if ((monkey_one != "y" and monkey_one != "n") or (monkey_two != "y" and monkey_two != "n")):
            print("Please enter a valid answer: y or n")
    elif monkey_one == "y" and monkey_two == "y":
        print("Uh Oh! We're in trouble!")
    elif monkey_one =="n" and monkey_two == "n":
        print("Uh Oh! We're in trouble!")
    else:
        print("Yay! We're going to have a good day!")

## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()   