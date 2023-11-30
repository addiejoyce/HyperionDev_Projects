import math

# Present the user with 2 calculation choices.

print('''
Investment: to calculate the amount of interest you'll earn on your investment.)   
Bond: to calculate the amount you'll have to pay on a home loan.
''')

# Use a while loop to enable the user to re-enter an incorrect string response.
# Add try/except block in case the user enters a non-numeric value when prompted.

while True:

    # Request the user to enter one of the two choices printed above.
    # Prevent letter case input errors by converting the user's response to .lower()

    choice = input("Enter Investment or Bond to proceed: ").lower()

    if choice == "bond":

        try:

            # Obtain investment amount, interest rate, and investment duration from the user.
            # Use an amortization accounting formula, where P = property value (or loan amount)
            # i = (interest rate ÷ 100) ÷ 12
            # n = number of repayment months

            P = float(input("Enter the current value of the property: "))

            i = float(input("Enter the interest rate amount (exclude the % sign): ")) / 100
            i = i / 12

            n = float(input("Enter the number of months you'll take to repay the bond: "))

        except ValueError:
            print("You've entered an invalid number.")
            continue

        # Calculate the above values to return the monthly repayment amount.
        repayment = (i * P) / (1 - (1 + i) ** (-n))

        print(f"Your monthly repayment amount will be {round(repayment, 2)}.")
        break

    elif choice == "investment":

        # Obtain the investment amount, interest rate, and investment years from the user
        # Where P = deposit amount, t = number of investment years, r = interest rate / 100

        try:

            P = float(input("Enter the amount you wish to deposit: "))

            r = float(input("Enter the interest rate amount (exclude the % sign) ")) / 100

            t = float(input("Enter the number of years you wish to invest for: "))

        except ValueError:
            print("You've entered an invalid number.")
            continue

        # Use the values above to calculate simple and compound interests and assign them to variables.

        simp_interest = P * (1 + r * t)
        comp_interest = P * math.pow((1 + r), t)

        # Use a nested loop to run the code for 'compound' and 'simple' interests.

        while True:

            interest = input("Select between simple and compound interest: ").lower()

            if interest == "compound":
                print(f"After {t} year(s) at a {r * 100}% interest rate you will have {
                    round(comp_interest, 2)}. ")
                break

            elif interest == "simple":
                print(f"After {t} year(s) at a {r * 100}% interest rate you will have {
                    round(simp_interest, )}.")
                break

            else:
                print("Error. ")
                continue
    else:
        print("Error. ")
        continue
    break
