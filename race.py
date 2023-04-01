#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:33:34 2023

@author: giannidiarbi

Gianni Diarbi
DS2000
Spring 2023
HW 7 Problem 2 
race.py - The Driver
"""

RUNNER_FILE = "runner_data.txt"

COLORS = ['royalblue', 'pink', 'mediumpurple', 'peru', 'seagreen']

import matplotlib.pyplot as plt

# from [filename] inport [classname]
from runner import Runner

def main():

    # Create empty lists to append runners to
    runners = []
    
    # Intiialize a counter variable for runners' colors and y-position
    counter = 0
    
    # Gather Data - Read in the file, skip the header, and assume one
    # runner per line
    with open(RUNNER_FILE, "r") as infile:
        header = infile.readline()
       
        for line in infile:
            line = line.strip().split(' ')
            name = ' '.join(line[0:2])
            
            # For each line in the file, create a Runner object, assign colors
            # and y-values for the plot, and keep all Runners in a list
            runner = Runner(name, color = COLORS[counter], y = counter + 1)
            counter += 1
            
            # Iterate over runs, adding one run to the list of runs - add 
            # every running distance to each runner's individual list of runs
            for run in line[2:]:
                runner.add_run(float(run))
            runners.append(runner)
    
    # Initialize the max distance ran and best runner             
    max_distance = 0
    best_runner = None
    
    # Find the runner who ran the farthest overall, and the max distance
    for runner in runners:
        total_distance = runner.get_total_distance()
   
        if total_distance > max_distance:
            max_distance = total_distance
            best_runner = runner
   
   # Iterate over every day in February
    for day in range(1, 29):
        
        # Create xlim and ylim values that are consistent for each plot
        plt.xlim(0, max_distance + 10)
        plt.ylim(-1, 9)
        
        # Generate plots, rendering all Runner objects and updating their 
        # x-values with daily run amounts 
        for runner in runners:
            runner.move_next()
            runner.draw()
            
        # Add a consistent legend, xlabel, and title
        plt.xlabel('Miles Traveled')
        plt.title('Miles Covered by Runners in February') 
        plt.legend(fontsize = 9)
        plt.show()
            
    # Print the name of the runner who ran the most miles in February
    print(best_runner)

main()
