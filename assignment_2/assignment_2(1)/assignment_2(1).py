#####################################################################################################################
#####################################################################################################################
# Objected Oriented Programming in Python

# Expected knowledge to resolve the first part of assignment:
# objected oriented programming in Python
# classes
# composition
# Inheritance
# polymorphism


# OBS: you need to verify your own code by
# constructing your object and calling its methods


#####################################################################################################################
#####################################################################################################################

# 1. Rectangle class
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area
# of a rectangle.

class Rectangle:
    # +++your code here+++
    pass


#####################################################################################################################
#####################################################################################################################

# 2. Deck class
# Create a deck of cards class. Internally, the deck of cards should use another
# class, a card class. Your requirements
# are:
# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all
# 52 cards and then rearranges them
# randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a
# value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
class Card:
    pass


class Deck:
    pass


#####################################################################################################################
#####################################################################################################################

# 3. Inheritance
# From the class Employee below create:


class Employee:
    def __init__(self, id_employee, name):
        self.id_employee = id_employee
        self.name = name


# a. a class SalaryEmployee that inherits from Employee adding a weekly_salary as an initiation attribute
# together with id, name
# For example: the construction of an object of the class SalaryEmployee will be like:
# salary_Andy = SalaryEmployee(1, 'Andy Smith', 500)
# id_employee, name, weekly_salary
# create a calculate_payroll method that returns the payment (i.e. weekly salary value)

class SalaryEmployee(Employee):
    def __init__(self, id_employee, name, weekly_salary):
        pass

    def calculate_payroll(self):
        pass


# b. a class HourlyEmployee
# the objective of this class if to calculate the payroll based in two attributes: hours_worked and hour_rate
# to that, this class will inherit from Employee and receive the as attribute the values hours_worked and hour_rate
# OBS: you need to create a calculate_payroll method for this class that takes into consideration the hours_worked and
# hour_rate to calculate the payment
class HourlyEmployee:
    pass


# c. a class CommissionEmployee
# the objective of this class if to calculate the payroll based in two attributes: weekly_salary and commission
# to that, this class will inherit from other class (which one do you think would be more appropriate?)
# and receive the values of weekly_salary and commission.
# OBS: you need to create a calculate_payroll method for this class that takes into consideration weekly_salary and
# commission to calculate the payment
class CommissionEmployee:
    pass


# 4. polymorphism
# Create/cite an example of Polymorphism in Python


#####################################################################################################################
#####################################################################################################################
#
# Pandas / Numpy / Dealing with datasets.
#
#####################################################################################################################
#####################################################################################################################

# 1. Import numpy and pandas on this document

# 2. Open the given dataset using Pandas (Forbes Global 2000 - 2019.csv)


data = pd.read_csv('dataset/Forbes_Global_2000_2019.csv')

#####################################################################################################################
# How to get information from a dataset using Pandas/numpy
#####################################################################################################################

# Using NumPy and Pandas, answer the following questions from the given dataset:

# what is the The cumulative market value of each industry?
# Which industry is the most profitable (in terms of revenue, profits) and which hold the highest asset value?
# Is there any correlation between profit and asset values?
# What are the Top 10 companies (names) that have
# a) highest profits as a % to assets; and
# b) highest profits as a % to revenue.
# Speculate what these might have in common, e.g. same industry, reside in same country, etc.


################################################################################################################
#
# SOME BASICS of plotting data with Python using Matplotlib
# Using the provided dataset (company_sales_data.csv)
#
################################################################################################################

# 1. Import matplotlib on this document

# 2. Read Total profit of all months and show it using a line plot
# Total profit data provided for each month. Generated line plot must include the following properties: –
#
# X label name = Month Number
# Y label name = Total profit

# 3. Get Total profit of all months and show line plot with the following Style properties
# Generated line plot must include following Style properties: –
#
# Line Style dotted and Line-color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker
# Line marker color as read
# Line width should be 3

# 4. Read all product sales data and show it  using a multiline plot

# 5. Read toothpaste sales data of each month and show it using a scatter plot
# Also, add a grid in the plot. gridline style should “–“

# 6. Read face cream and facewash product sales data and show it using the bar chart
# Bar chart should display the number of units sold per month for each product.
# Add a separate bar for each product in the same chart.

# 7. Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk

# 8. Read the total profit of each month and show it using the histogram to see most common profit ranges

# 9. Calculate total sale data for last year for each product and show it using a Pie chart
# Note: In Pie chart display Number of units sold per year for each product in percentage.

# 10. Read Bathing soap facewash of all months and display it using the Subplot

# 11.  Read all product sales data and show it using the stack plot
