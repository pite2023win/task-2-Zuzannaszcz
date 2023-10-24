#
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Bank:
  def __init__(self, people_list ):
    self.people_list = people_list

class Person:
  def __init__(self, name, money ):
    self.name = name
    self.money = money

if __name__ == "__main__":

  print("do you want to create a bank? type: yes or no")
  answer = input()
  while answer == "yes":
    print(f"chose the name of a bank")
    bank_name = input()
    bank_name = Bank([])
    print("do you want to create another one? type: yes or no")
    answer = input()

  print("do you want to create a person? type: yes or no")
  answer = input()
  while answer == "yes":
    print(f"chose the name of a person")
    person_name = input()
    print(f"amount of money?")
    money = input()
    person_name = Person(person_name, money)
    print("do you want to create another one? type: yes or no")
    answer = input()

  print(f"chose the name of a person")
  person_name = input()
  print(f"amount of money?")
  money = input()
  person_name = Person(person_name, money)

  print("do you want add any person to a bank? type: yes or no")
  answer = input()
  while answer == "yes":
    print("do you want to add another one? type: yes or no")
    answer = input()
