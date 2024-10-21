import meal

def display_meals(plan, name):
    print(name, end = ": ")
    print(plan)
    meal.get_meals(14, 5)

display_meals("14-Punch", "JMU Duke")