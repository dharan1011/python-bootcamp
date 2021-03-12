"""
* To resuse code
* To write code modularly
"""
def calculate_tip(meal_cost, tip_percentage):
    tip = tip_percentage / 100 * meal_cost
    return tip
    
meal_cost = float(input())
tip_percentage = float(input())
tip = calculate_tip(meal_cost, tip_percentage)
tip1 = calculate_tip(meal_cost, tip_percentage)
total_cost = meal_cost + tip + tip1
print("Total Cost :", total_cost)