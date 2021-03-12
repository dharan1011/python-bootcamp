# Write a program to calculate the total cost of the order
# a item has a cost which is taken from user
# 18% of tax is apppied on each item

def calculate_tax(item_cost, tax_percentage):
    return tax_percentage / 100 * item_cost

no_of_items = int(input())
total_cost = 0
tax_percentage = 18
for x in range(no_of_items):
    item_cost = float(input())
    item_tax = calculate_tax(item_cost, tax_percentage)
    total_item_cost = item_cost + item_tax
    total_cost += total_item_cost

print("Total :", total_cost)


