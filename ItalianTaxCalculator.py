# Italian Tax and Financial Efficiency Calculator
# By Cyb3r00v3

TAX_BRACKETS = [(15000, 0.23), (28000, 0.27), (55000, 0.38), (75000, 0.41), (None, 0.43)]

def calculate_tax(gross_pay):
    """Calculate tax based on gross pay and tax brackets."""
    tax = 0
    for bracket in TAX_BRACKETS:
        if gross_pay <= 0:
            break
        if bracket[0] is None:
            tax += gross_pay * bracket[1]
        else:
            if gross_pay > bracket[0]:
                tax += bracket[0] * bracket[1]
                gross_pay -= bracket[0]
            else:
                tax += gross_pay * bracket[1]
                break
    return tax

def calculate_living_expenses():
    """Calculate estimated monthly living expenses based on common factors."""
    housing = 800  # Average monthly rent or mortgage payment
    food = 300     # Monthly grocery expenses
    transportation = 100  # Monthly transportation expenses (public transport, fuel, etc.)
    utilities = 150   # Monthly utility bills (electricity, water, internet, etc.)
    other_necessities = 200  # Miscellaneous monthly expenses (clothing, healthcare, etc.)

    total_expenses = housing + food + transportation + utilities + other_necessities
    return total_expenses

def suggest_distribution(gross_pay):
    """Suggest the best way to distribute income for financial efficiency."""
    tax = calculate_tax(gross_pay)
    living_expenses = calculate_living_expenses()
    remaining_income = gross_pay - tax - living_expenses
    return remaining_income

def display_ascii_art():
    """Display ASCII art."""
    print("""
    ***************************************
    *    Italian Tax & Financial Calc     *
    ***************************************
    """)

def main():
    display_ascii_art()
    
    # Input yearly gross pay
    yearly_gross_pay_str = input("Enter your yearly gross pay in Euros: €")
    yearly_gross_pay_str = yearly_gross_pay_str.replace('€', '').replace(',', '')
    try:
        yearly_gross_pay = float(yearly_gross_pay_str)
    except ValueError:
        print("Invalid input. Please enter a valid number for the yearly gross pay.")
        return

    # Calculate monthly gross pay, total tax, living expenses, and suggest income distribution
    monthly_gross_pay = yearly_gross_pay / 12
    total_tax = calculate_tax(yearly_gross_pay)
    total_living_expenses = calculate_living_expenses()
    suggested_distribution = suggest_distribution(yearly_gross_pay)
    
    # Calculate take-home pay
    take_home_pay = yearly_gross_pay - total_tax
    
    # Display results
    print("\nResults\t\tYearly\t\tMonthly")
    print(f"Gross Pay\t€{yearly_gross_pay:.2f}\t€{monthly_gross_pay:.2f}")
    print(f"Total Tax\t€{total_tax:.2f}\t€{total_tax / 12:.2f}")
    print(f"Living Expenses\t\t\t€{total_living_expenses:.2f}\t€{total_living_expenses / 12:.2f}")
    print(f"Take-Home\t€{take_home_pay:.2f}\t€{take_home_pay / 12:.2f}")
    print(f"Suggested Distribution (after tax and living expenses): €{suggested_distribution:.2f}")
    
    print("\nNote: The deductions used in the calculator assume you are not married and have no dependents.")
    print("You may pay less if tax credits or other deductions apply.")

if __name__ == "__main__":
    main()
