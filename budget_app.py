import budget
from budget import create_spend_chart
from unittest import main

class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = self.get_balance()
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
    
    final = title + items + "Total: " + str(total)
    return final

  
  def deposit(self, amount, description = ""):
    self.ledger.append({'amount': amount, 'description': description})
  
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
  
  def get_balance(self):
    total = 0
    for item in self.ledger:
      total += item["amount"]
    return total

  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to: " + destination.name)
      destination.deposit(amount, "Transfer from: " + self.name)
      return True
    return False

  def check_funds(self, amount):
    total = 0
    for item in self.ledger:
      total += item["amount"]
    if total >= amount:
      return True
    return False
  
  def total_withdraw(self):
    total = 0
    for item in self.ledger():
      if item['amount'] < 0:
        total += item['amount']
    return total


food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
