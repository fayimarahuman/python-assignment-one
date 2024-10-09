#1a.The volume of a sphere with radius r is (4/3)*pie * r**2. What is the volume of the sphere with radius 5
#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places.
r=int(input('Enter the radius:'))
volume_of_a_sphere=(4/3)*3.14*r**2
print (f'the volume of the sphere with radius 5 is:  {volume_of_a_sphere :.2f}')
#2.create a program to calculate the area of a triangle(1/2*base*height).base and height should be entered using the keyboard.
base=int(input('enter the base:'))
height=int(input('enter the height:'))
area_of_a_triangle=(1/2*base*height)
print(f'the area of a triangle is:{area_of_a_triangle}')
#3.WITI has tasked you to automate a simple grading system, as a python student write a program using to display the grades that the students will be receiving based on the mark scored in a subject.the grades are;
#90%-100% Grade is A
#80%-89% Grade is B
#70%-79% Grade is C
#60%-69% Grade is D
#50%-59% Grade is E
#<50% Fail.
score=int(input("enter the student's score:\t"))
if 90<=score<=100:
    print("Grade is A")
elif 80<=score<=89:
    print("Grade is B")
elif 70<=score<=79:
    print("grade is C")
elif 60<=score<=69:
    print("Grade is D")
elif 50<=score<=59:
    print("Grade is E")
else:
    print("Fail")
#question 4
#WITI Academy is proposing a sacco to help students save their money.
#Design a platform that will do the following.
#Welcome to, WITI Academy Sacco
#1. Deposit Money
#2.With draw money
#3. Check balance
#Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000
#If  the students selects 2, money should be withdrawn and the minimum withdraw is  500
#If the student selects 3, the account balance should be displayed
def sacco_transaction():
    account_balance = 0  # Initialize account balance as 0

    while True:
        print("\nWelcome to WITI Academy Sacco")
        print("Please choose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")  # Option to exit the loop
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            deposit_amount = float(input("Enter amount to deposit: "))
            if deposit_amount >= 1000:
                account_balance += deposit_amount
                print(f"Successfully deposited {deposit_amount:,.2f}. New balance is {account_balance:,.2f}.")
            else:
                print("Minimum deposit amount is 1000.")

        elif choice == "2":
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount >= 500:
                if account_balance >= withdraw_amount:
                    account_balance -= withdraw_amount
                    print(f"Successfully withdrew {withdraw_amount:,.2f}. New balance is {account_balance:,.2f}.")
                else:
                    print("Insufficient balance.")
            else:
                print("Minimum withdraw amount is 500.")

        elif choice == "3":
            print(f"Your current balance is {account_balance:,.2f}.")
        
        elif choice == "4":
            print("Thank you for using WITI Academy Sacco. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid choice. Please try again.")
        

# Call the function to run the program
sacco_transaction()