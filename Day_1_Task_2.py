square_feet = int(input("Enter square feet to be   painted:"))
price_of_the_paint_per_gallon = int(input("Enter the price of paint:"))
number_of_gallons = square_feet / 115
hours_of_labor = number_of_gallons * 8
cost_of_the_paint = number_of_gallons * price_of_the_paint_per_gallon
labor_charges = hours_of_labor * 20
total_cost_of_the_paint_job = labor_charges * cost_of_the_paint
print(number_of_gallons)
print(hours_of_labor)
print(cost_of_the_paint)
print(labor_charges)
print(total_cost_of_the_paint_job)
