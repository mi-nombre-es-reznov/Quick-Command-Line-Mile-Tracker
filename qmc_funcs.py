# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:50:17 2020

@author: 06878
"""
from os import system, name
import time
import re
import datetime
import qmc_consts as consts

def validate_email(test_email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(re.search(regex,test_email)):
        return True          
    else:
        return False

def wait(l):
    time.sleep(l)
    
# define our clear function
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def get_user_data():
    f = ""
    l = ""
    e = ""
    d = ""
    check = False
    
    while(f == ""):
        f = input("What is your First name? ")
    
    while(l == ""):
        l = input("What is your Last name? ")
        
    while(e == "" or check == False):
        e = input("What is your email address? ")
        
        check = validate_email(e)
        
        if(check == False):
            clear()
            print("Invalid email. Please follow the format of: user@email.com")
        
    x = datetime.datetime.now()
    d = (get_month_name(int(x.month)) + " " + str(x.year))
    
    return f, l, e, d

def get_month_name(num):
    if(num == 1):
        return "January"
    elif(num == 2):
        return "February"
    elif(num == 3):
        return "March"
    elif(num == 4):
        return "April"
    elif(num == 5):
        return "May"
    elif(num == 6):
        return "June"
    elif(num == 7):
        return "July"
    elif(num == 8):
        return "August"
    elif(num == 9):
        return "September"
    elif(num == 10):
        return "October"
    elif(num == 11):
        return "November"
    elif(num == 12):
        return "December"

def Menu(opt):
    '''
    - Input -
    opt -- List: Holds the names of the Menu items being passed in.
    choice -- Integer: Holds the representative value of the Menu item the user chose.
    
    - Output -
    ret: choice
    '''
    choice = 0
    
    # Iterate through the menu and display the number of items with choice marker
    for i in range(len(opt)):
        print(str(i + 1) + ") " + str(opt[i]))
        
    # Menu space
    print("\n\n")
        
    # Bound check for valid choice
    while(choice < 1 or choice > len(opt)):
        try:
            # Accept user input as an int and force repeat entry if invalid
            choice = int(input("Please select an option: "))
        except ValueError:
            choice = 0
            
    return choice

def get_vehicle_data():
    make = ""
    model = ""
    year = 0
    
    x = datetime.datetime.now()

    while(make == ""):
        make = input("What make is your vehicle? ")

    while(model == ""):
        model = input("What model is your vehicle? ")

    while(year < 1950 or year > (int(x.year) + 1)):
        try:
            year = int(input("What year is your vehicle? "))
        except ValueError:
            clear()
            year = 0
            print("Invalid year. Enter a year between 1950 and " + str(int(x.year) + 1) + "\n")
            
    return make, model, str(year)

def y_n_choice(m):
    choice = ""
    
    while(choice != 'n' and choice != 'y'):
        choice = input(m + " [Y/n]? ")
        choice = choice.lower()
    
    return choice

def get_start():
    stmi = 0
    sttime = ""
    
    while(stmi == 0):
        try:
            stmi = int(input("Starting miles: "))
        except ValueError:
            clear()
            print("Enter a valid number.\n")
            
    x = datetime.datetime.now()
    sttime = str(x.now())
    clear()
    
    return stmi, sttime

def get_end():
    emi = 0
    pay = 0.0
    etime = ""
    
    while(emi == 0):
        try:
            emi = int(input("Ending miles: "))
        except ValueError:
            clear()
            print("Enter a valid number.\n")
            
    while(pay == 0):
        try:
            pay = float(input("Shift pay: $"))
        except ValueError:
            clear()
            print("Enter a valid number.\n")
            
    x = datetime.datetime.now()
    etime = str(x.now())
    clear()
    
    return emi, etime, pay
    
def calc_shift(st, end, pay):
    tot_miles = 0
    saved = 0.0
    profit = 0.0
    owe = 0.0
    earn = 0.0
    
    tot_miles = (end - st)
    saved = (tot_miles * consts.MILE_WRITEOFF_2020)
    profit = (pay - saved)
    owe = (profit * (consts.SELF_EMPLOYEMENT_TWO + consts.INCOME_TAX_TWO))
    earn = (profit - owe)
    
    return saved, owe, earn