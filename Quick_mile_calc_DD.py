# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:21:00 2020

@author: Nicholas Perez-Aguilar

Description: This program is used as a quick method to enter information about
a vehicle's Odometer to calculate amount of write-offs in taxes

Features:
    1) Calculate start and end miles on the Odometer and finds the total miles
        for the job.
    2) Calculates the amount saved in taxes based on total miles driven
    3) Adds a start and end timestamp with data entry
    4) All data is written to a .csv file
    5) Statistics can be calculated off data in .csv file
"""
import qmc_consts as qc
import qmc_funcs as qf
import qmc_Menus as Menu
import time
import csv

class get_info:
    def __init__(self, f, l, e, j, ma, mo, y):
        '''
        

        Parameters
        ----------
        f : String
            First Name of user.
        l : String
            Last Name of user.
        e : String
            Email of user.
        j : String
            Join month and year of user.
        ma : String
            Make of vehicle.
        mo : String
            Model of vehicle.
        y : INT
            Year of vehicle.

        Returns
        -------
        None.

        '''
        self.first = f
        self.last = l
        self.email = e
        self.joined = j
        self.make = ma
        self.model = mo
        self.year = y

    def new_user():
        pass
    
    def new_car():
        pass
        
    def show_info(self):
        '''
        

        Returns
        -------
        None.

        '''
        print("Driver: " + self.first + " " + self.last)
        print("Email: " + self.email)
        print("Vehicle: " + self.year + " " + self.make + " " + self.model)
        print("Joined: " + self.joined)
        print('\n')
        
    def ret_info_user(self):
        return [self.first, self.last, self.email, self.joined]
    
    def ret_info_vehicle(self):
        return [self.make, self.model, self.year]

def Main():
    correct = ""
    
    # Test file for names
    try:
        file = open(qc.USER_INFO_FILE, 'r')
        print("File: " + qc.USER_INFO_FILE + " exists!")
    except FileNotFoundError:
        print("File doesn't exist! Creating files", end="", flush = True)
        qf.wait(2)
        
        for i in range(3):
            print(".", end='', flush=True)
            qf.wait(1)
        
        with open(qc.USER_INFO_FILE, 'a', newline = '') as file:
            writes = csv.writer(file)
            writes.writerow(qc.USER_INFO_HEADING)
            
        qf.clear()
        
        print("File: '" + qc.USER_INFO_FILE + "' has been successfully created.", flush = True)
        
        with open(qc.VEHICLE_INFO_FILE, 'a', newline = '') as file:
            writes = csv.writer(file)
            writes.writerow(qc.VEHICLE_INFO_HEADING)
                    
        print("File: '" + qc.VEHICLE_INFO_FILE + "' has been successfully created.", flush = True)
        qf.wait(2)
        qf.clear()
        Menu.new_account()
        f, l, e, d = qf.get_user_data()
        qf.clear()
        Menu.new_account()
        ma, mo, y = qf.get_vehicle_data()
        qf.clear()
        
        init_user = get_info(f, l, e, d, ma, mo, y)
        init_user.show_info()
        
        correct = qf.y_n_choice("Is data correct")
        
        if(correct == 'y'):
            with open(qc.USER_INFO_FILE, 'a', newline = '') as file:
                writes = csv.writer(file)
                writes.writerow(init_user.ret_info_user())
            
            with open(qc.VEHICLE_INFO_FILE, 'a', newline = '') as file:
                writes = csv.writer(file)
                writes.writerow(init_user.ret_info_vehicle())
            
            qf.clear()
            print("Data written successfully!")
            qf.wait(2)
        else:
            qf.clear()
            print("Data update not available! Please delete file (" + qc.USER_INFO_FILE + ") and start over.")
    
    # Main Menu    
    qf.clear()
    Menu.Main_Menu()
    
   
if(__name__ == "__main__"):
    qf.clear()
    Main()