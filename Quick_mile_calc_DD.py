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
class get_info:
    def __init__(self, f, l, j, ma, mo, y):
        '''
        

        Parameters
        ----------
        f : String
            First Name of user.
        l : String
            Last Name of user.
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
        self.joined = j
        self.make = ma
        self.model = mo
        self.year = y
        
    def show_info(self):
        
        print("Driver: " + self.first + " " + self.last)
        print("Vehicle: " + self.year + " " + self.make + " " + self.model + "\n")
        print("Joined: " + self.joined)