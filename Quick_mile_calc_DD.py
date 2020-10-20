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
import csv

fname = ""

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
    global fname
    correct = ""
    
    # Test file for names
    try:
        file = open(qc.USER_INFO_FILE, 'r')
        print("File: " + qc.USER_INFO_FILE + " exists!")
        
        with open(qc.USER_INFO_FILE, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for i in csv_reader:
                fname = i[0]
                print(fname)
            
    except FileNotFoundError:
        print("File doesn't exist! Creating files", end="", flush = True)
        qf.wait(2)
        
        for i in range(3):
            print(".", end='', flush=True)
            qf.wait(1)

        qf.clear()
        
        with open(qc.USER_INFO_FILE, 'a', newline = '') as file:
            writes = csv.writer(file)
            writes.writerow(qc.USER_INFO_HEADING)
                    
        print("File: '" + qc.USER_INFO_FILE + "' has been successfully created.", flush = True)
        
        with open(qc.VEHICLE_INFO_FILE, 'a', newline = '') as file:
            writes = csv.writer(file)
            writes.writerow(qc.VEHICLE_INFO_HEADING)
                    
        print("File: '" + qc.VEHICLE_INFO_FILE + "' has been successfully created.", flush = True)

        with open(qc.BASE_DATA_TRACKER, 'a', newline = '') as file:
            writes = csv.writer(file)
            writes.writerow(qc.BASE_DATA_HEADING)
                    
        print("File: '" + qc.BASE_DATA_TRACKER + "' has been successfully created.", flush = True)

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
    
    # Data values
    begin = 0
    end = 0
    sttime = ""
    endtime = ""
    tax_saved = 0
    pay = 0
    tax_owed = 0
    earnings = 0        
    
    # Main Menu    
    qf.clear()
    Menu.Main_Menu()
    print("Welcome " + fname + '\n')
    option = qf.Menu(qc.MM_OPTIONS)
    
    if(option == 1):
        begin, sttime = qf.get_start()
        end, endtime, pay = qf.get_end()
        tax_saved, tax_owed, earnings = qf.calc_shift(begin, end, pay)
        
        with open(qc.BASE_DATA_TRACKER, 'a', newline = '') as file:
            writes = csv.writer(file)
            writes.writerow([begin, end, sttime, endtime, '2020', tax_saved, tax_owed, '1', earnings])
        
    print("Starting miles: " + str(begin))
    print("Start Time: " + sttime)
    print("End miles: " + str(end))
    print("End Time: " + endtime)
    print("Saved: " + str(tax_saved))
    print("Owed: " + str(tax_owed))
    print("Earned" + str(earnings))
        
    
   
if(__name__ == "__main__"):
    qf.clear()
    Main()