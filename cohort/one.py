# Write a program to calculate tip for give meal price

meal_price = float(input())
tip_percentage = float(input())
tip = (tip_percentage / 100) * meal_price
total_cost = meal_price + tip
print(total_cost)