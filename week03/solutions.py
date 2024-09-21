import pandas as pd
import matplotlib.pyplot as plt

def question1():
    data = pd.read_csv("ProgrammingAssignment_MLAIFNCE9015.csv")
    product_list = data.values.tolist()
    cumulativeProfit = 0
    for x in product_list:
        if x[6] == "Food":
            cumulativeProfit += x[2]
    return cumulativeProfit
# print(question1())

def question2():
    data = pd.read_csv("ProgrammingAssignment_MLAIFNCE9015.csv")
    product_list = data.values.tolist()
    product_name = []
    for x in product_list:
        profitLists = x[2:6]
        if max(profitLists) != profitLists[-1]:
            product_name.append(x[1])
    return product_name
# print(question2())

def question3():
    data = pd.read_csv("ProgrammingAssignment_MLAIFNCE9015.csv")
    product_list = data.values.tolist()
    product_number = 0
    product_name = []
    for x in product_list:
        if x[6] == "Baby" or x[6] == "Luxury" or x[6] == "Food":
            product_number += 1
            product_name.append(x[1])
    return product_name
# print(question3())

def question4():
    data = pd.read_csv("ProgrammingAssignment_MLAIFNCE9015.csv")
    product_list = data.values.tolist()
    profit_food = 0
    profit_luxury = 0
    profit_baby = 0
    profit_personal_care = 0
    for x in product_list:
        if x[6] == "Food":
            profit_food += x[4]
        elif x[6] == "Luxury":
            profit_luxury += x[4]
        elif x[6] == "Baby":
            profit_baby += x[4]
        else:
            profit_personal_care += x[4]

    profit_numbers = [profit_food, profit_luxury, profit_baby, profit_personal_care]
    product_category = ["Food", "Luxury", "Baby", "Personal Care"]

    plt.bar(product_category, profit_numbers)
    plt.title("Q3 Profit in different categories")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.show()
question4()